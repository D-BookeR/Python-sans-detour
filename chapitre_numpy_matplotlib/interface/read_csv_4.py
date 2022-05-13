import os
import sys
import urllib.request
import ssl
import zipfile
import certifi
import numpy
import matplotlib.pyplot

NB_CELLULE_H = 10
URL_SITE = "https://www.insee.fr/fr/statistiques/series/csv/famille/102775111"


def lecture_csv(url_site, origine=0, nb_ligne=101, liste_classe=[0, 1]):
    contexte_local = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                                cafile=certifi.where())
    contexte_local.check_hostname = True
    contexte_local.verify_mode = ssl.CERT_REQUIRED

    try:
        with urllib.request.urlopen(url_site,
                                    context=contexte_local) as response:
            fichier_archive = response.read()
    except urllib.error.URLError:
        print(sys.exc_info())
        print("Problème de lecture de l'URL : ", url_site)
        sys.exit()
    try:
        with open("test.zip", "wb") as f:
            f.write(fichier_archive)
    except OSError:
        print(sys.exc_info())
        print("Problème de lecture de l'URL : ", url_site)
        sys.exit()
    nom_fichier_csv = "valeurs_annuelles.csv"
    try:
        with zipfile.ZipFile("test.zip", "r") as mon_archive:
            mon_archive.extract(nom_fichier_csv)
        os.remove("test.zip")
    except FileNotFoundError:
        print(sys.exc_info())
        print("archive non trouvée")
        sys.exit()
    except (KeyError, ValueError):
        print(sys.exc_info())
        print("Problème d'extraction de : ", nom_fichier_csv)
        sys.exit()
    val_csv = numpy.genfromtxt(nom_fichier_csv,
                               delimiter=';',
                               dtype=numpy.str_,
                               encoding='utf-8'
                               )
    os.remove(nom_fichier_csv)
    val_csv[val_csv == '""'] = "0"
    x_annee = numpy.array([numpy.int32(v.replace('"', ''))
                           for v in val_csv[0, 4:]])
    val_csv = val_csv[1::2, :]
    nb_elt_classe = 117
    population = numpy.zeros(shape=(nb_ligne, x_annee.shape[0]),
                             dtype=numpy.single)
    titre_courbe = [v.replace('"', '')
                    for v in val_csv[origine: origine + nb_ligne, 0]]
    titre_courbe = [v[2] for v in numpy.char.split(titre_courbe, ' - ')]
    for ind in liste_classe:
        y_val = val_csv[ind * nb_elt_classe + origine:
                        ind * nb_elt_classe + origine + nb_ligne,
                        4:]
        for ind_ligne in range(nb_ligne):
            nb = [numpy.int32(v.replace('"', ''))
                  for v in y_val[ind_ligne, :]]
            population[ind_ligne, :] += numpy.array(nb)
    return population, x_annee, titre_courbe


def tracer_toutes_courbes(population, titre):
    nb_ligne_graphique = (nb_dpt - 1) // NB_CELLULE_H + 1
    fig, ax = matplotlib.pyplot.subplots(nrows=nb_ligne_graphique,
                                         ncols=NB_CELLULE_H)
    for ind, val_pop in enumerate(population):
        ind_lig, ind_col = divmod(ind, NB_CELLULE_H)
        ax[ind_lig][ind_col].plot(x_annee, val_pop, label=titre[ind])
        ax[ind_lig][ind_col].tick_params(axis='both', labelsize=5)
        exposant = ax[ind_lig][ind_col].yaxis.get_offset_text()
        exposant.set_size(5)
        ax[ind_lig][ind_col].legend(loc='lower left', fontsize=5)
    for ind in range(nb_dpt, NB_CELLULE_H * nb_ligne_graphique):
        ind_lig, ind_col = divmod(ind, NB_CELLULE_H)
        fig.delaxes(ax[ind_lig][ind_col])
    return fig, ax


def act_bt_suivant(event, extra):
    extra[0] += 1
    extra[0] = extra[0] % nb_dpt
    texte_bouton(extra)
    tracer_case(extra)
    matplotlib.pyplot.draw()


def act_bt_precedent(event, extra):
    extra[0] -= 1
    extra[0] = extra[0] % nb_dpt
    texte_bouton(extra)
    tracer_case(extra)
    matplotlib.pyplot.draw()


def act_visible(label, extra):
    extra[2][extra[0]] = not extra[2][extra[0]]
    tracer_case(extra)
    tracer_courbe(extra)
    matplotlib.pyplot.draw()


def tracer_case(extra):
    case_visible.lines[0][0].set_visible(extra[2][extra[0]])
    case_visible.lines[0][1].set_visible(extra[2][extra[0]])


def texte_bouton(extra):
    bt_suivant.label.set_text(extra[6][(extra[0] + 1) % nb_dpt])
    bt_precedent.label.set_text(extra[6][(extra[0] - 1) % nb_dpt])
    case_visible.labels[0].set_text(extra[6][extra[0]])


def tracer_courbe(extra):
    for courbe in extra[1]:
        for c in courbe:
            c.remove()
    if extra[3].get_legend():
        extra[3].get_legend().remove()
    extra[1].clear()
    liste_legende = []
    extra[3].set_prop_cycle(None)
    for ind, status in enumerate(extra[2]):
        if status:
            courbe = extra[3].plot(extra[5], extra[4][ind, :], lw=2)
            extra[1].append(courbe)
            liste_legende.append(extra[6][ind])
    if liste_legende:
        extra[3].legend(liste_legende)
    extra[3].relim()


def click_souris(event, extra_data):
    lig_col = numpy.argwhere(extra_data[8] == event.inaxes)
    if lig_col.shape[0] == 1:
        extra_data[0] = lig_col[0, 0] * NB_CELLULE_H + lig_col[0, 1]
        extra_data[2][extra_data[0]] = not extra_data[2][extra_data[0]]
        texte_bouton(extra_data)
        tracer_case(extra_data)
        tracer_courbe(extra_data)
        extra_data[7].canvas.draw_idle()


if __name__ == "__main__":
    dpt_origine = 0
    nb_dpt = 101
    population_cumul, x_annee, titre_courbe = lecture_csv(URL_SITE,
                                                          dpt_origine,
                                                          nb_dpt,
                                                          [0, 1])
    fig_toutes, glb_ax = tracer_toutes_courbes(population_cumul, titre_courbe)
    courbe_visible = numpy.zeros(shape=nb_dpt, dtype=numpy.bool_)
    fig_selec, ax_selec = matplotlib.pyplot.subplots()
    matplotlib.pyplot.subplots_adjust(bottom=0.2)
    liste_courbes = []
    extra_data = [0, liste_courbes, courbe_visible,
                  ax_selec, population_cumul, x_annee,
                  titre_courbe, fig_selec, glb_ax]
    axe_bout_precedent = matplotlib.pyplot.axes([0.56, 0.05, 0.1, 0.075])
    axe_bout_suivant = matplotlib.pyplot.axes([0.81, 0.05, 0.1, 0.075])
    axe_case_visible = matplotlib.pyplot.axes([0.67, 0.05, 0.13, 0.075])
    bt_suivant = matplotlib.widgets.Button(axe_bout_suivant,
                                           titre_courbe[(extra_data[0] + 1) %
                                                        nb_dpt])
    bt_suivant.label.set_fontsize(5)
    bt_suivant.on_clicked(lambda x: act_bt_suivant(x, extra_data))
    bt_precedent = matplotlib.widgets.Button(axe_bout_precedent,
                                             titre_courbe[(extra_data[0] - 1) %
                                                          nb_dpt])
    bt_precedent.label.set_fontsize(5)
    bt_precedent.on_clicked(lambda x: act_bt_precedent(x, extra_data))
    case_visible = matplotlib.widgets.CheckButtons(
                      axe_case_visible,
                      [titre_courbe[extra_data[0]]],
                      [courbe_visible[extra_data[0]]])
    case_visible.labels[0].set_fontsize(5)
    case_visible.on_clicked(lambda x: act_visible(x, extra_data))
    fig_toutes.canvas.mpl_connect('button_press_event',
                                  lambda x: click_souris(x, extra_data))
    matplotlib.pyplot.show()
