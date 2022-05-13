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
    contexte_local = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
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
    x_annee =\
        numpy.array([numpy.int32(v.replace('"', '')) for v in val_csv[0, 4:]])
    val_csv = val_csv[1::2, :]
    nb_elt_classe = 117
    population =\
        numpy.zeros(shape=(nb_ligne, x_annee.shape[0]), dtype=numpy.single)
    titre_courbe =\
        [v.replace('"', '') for v in val_csv[origine: origine + nb_ligne, 0]]
    titre_courbe = [v[2] for v in numpy.char.split(titre_courbe, ' - ')]
    for ind in liste_classe:
        y_val = val_csv[
            ind * nb_elt_classe + origine:
            ind * nb_elt_classe + origine + nb_ligne, 4:]
        for ind_ligne in range(nb_ligne):
            nb = [numpy.int32(v.replace('"', '')) for v in y_val[ind_ligne, :]]
            population[ind_ligne, :] += numpy.array(nb)
    return population, x_annee, titre_courbe


class FichierINSEE:
    def __init__(self, url_site, dpt_origine, nb_dpt, liste_classe):
        self.ind = 0
        self.nb_ligne = nb_dpt
        self.liste_courbe = []
        self.population_cumul, self.x_annee, self.titre_courbe = \
            lecture_csv(url_site, dpt_origine, self.nb_ligne, liste_classe)
        fig_toutes, self.glb_ax = self.tracer_toutes_courbes()
        self.courbe_visible = numpy.zeros(shape=self.nb_ligne,
                                          dtype=numpy.bool_)
        self.fig_selec, self.ax_selec = matplotlib.pyplot.subplots()
        matplotlib.pyplot.subplots_adjust(bottom=0.2)
        axe_bout_precedent = matplotlib.pyplot.axes([0.56, 0.05, 0.1, 0.075])
        axe_bout_suivant = matplotlib.pyplot.axes([0.81, 0.05, 0.1, 0.075])
        axe_case_visible = matplotlib.pyplot.axes([0.67, 0.05, 0.13, 0.075])
        self.bt_suivant = \
            matplotlib.widgets.Button(
                axe_bout_suivant,
                self.titre_courbe[(self.ind + 1) % self.nb_ligne])
        self.bt_suivant.label.set_fontsize(5)
        self.bt_suivant.on_clicked(self.act_bt_suivant)
        self.bt_precedent = \
            matplotlib.widgets.Button(
                axe_bout_precedent,
                self.titre_courbe[(self.ind - 1) % self.nb_ligne])
        self.bt_precedent.label.set_fontsize(5)
        self.bt_precedent.on_clicked(self.act_bt_precedent)
        self.case_visible = \
            matplotlib.widgets.CheckButtons(
                axe_case_visible,
                [self.titre_courbe[self.ind]],
                [self.courbe_visible[self.ind]]
                )
        self.case_visible.labels[0].set_fontsize(5)
        self.case_visible.on_clicked(self.act_visible)
        fig_toutes.canvas.mpl_connect('button_press_event', self.click_souris)

    def tracer_toutes_courbes(self):
        nb_ligne_graphique = (self.nb_ligne - 1) // NB_CELLULE_H + 1
        fig, ax = matplotlib.pyplot.subplots(nrows=nb_ligne_graphique,
                                             ncols=NB_CELLULE_H)
        for ind, population in enumerate(self.population_cumul):
            ind_lig, ind_col = divmod(ind, NB_CELLULE_H)
            ax[ind_lig][ind_col].plot(self.x_annee,
                                      population,
                                      label=self.titre_courbe[ind])
            ax[ind_lig][ind_col].tick_params(axis='both', labelsize=5)
            exposant = ax[ind_lig][ind_col].yaxis.get_offset_text()
            exposant.set_size(5)
            ax[ind_lig][ind_col].legend(loc='lower left', fontsize=5)
        for ind in range(self.nb_ligne, NB_CELLULE_H * nb_ligne_graphique):
            ind_lig, ind_col = divmod(ind, NB_CELLULE_H)
            fig.delaxes(ax[ind_lig][ind_col])
        return fig, ax

    def act_bt_suivant(self, event):
        self.ind += 1
        self.ind = self.ind % self.nb_ligne
        self.texte_bouton()
        self.tracer_case()
        matplotlib.pyplot.draw()

    def act_bt_precedent(self, event):
        self.ind -= 1
        self.ind = self.ind % self.nb_ligne
        self.texte_bouton()
        self.tracer_case()
        matplotlib.pyplot.draw()

    def act_visible(self, label):
        self.courbe_visible[self.ind] = not self.courbe_visible[self.ind]
        self.tracer_case()
        self.tracer_courbe()
        matplotlib.pyplot.draw()

    def tracer_case(self):
        self.case_visible.lines[0][0].set_visible(
            self.courbe_visible[self.ind])
        self.case_visible.lines[0][1].set_visible(
            self.courbe_visible[self.ind])

    def texte_bouton(self):
        self.bt_suivant.label.set_text(
            self.titre_courbe[(self.ind + 1) % self.nb_ligne])
        self.bt_precedent.label.set_text(
            self.titre_courbe[(self.ind - 1) % self.nb_ligne])
        self.case_visible.labels[0].set_text(self.titre_courbe[self.ind])

    def tracer_courbe(self):
        for courbe in self.liste_courbe:
            for c in courbe:
                c.remove()
        if self.ax_selec.get_legend():
            self.ax_selec.get_legend().remove()
        self.liste_courbe.clear()
        liste_legende = []
        self.ax_selec.set_prop_cycle(None)
        for ind, status in enumerate(self.courbe_visible):
            if status:
                courbe = self.ax_selec.plot(
                    self.x_annee,
                    self.population_cumul[ind, :],
                    lw=2)
                self.liste_courbe.append(courbe)
                liste_legende.append(self.titre_courbe[ind])
        if liste_legende:
            self.ax_selec.legend(liste_legende)
        self.ax_selec.relim()

    def click_souris(self, event):
        lig_col = numpy.argwhere(self.glb_ax == event.inaxes)
        if lig_col.shape[0] == 1:
            self.ind = lig_col[0, 0] * NB_CELLULE_H + lig_col[0, 1]
            self.courbe_visible[self.ind] = not self.courbe_visible[self.ind]
            self.texte_bouton()
            self.tracer_courbe()
            self.fig_selec.canvas.draw_idle()


if __name__ == "__main__":
    mon_interface = FichierINSEE(URL_SITE, 0, 101, [0, 1])
    matplotlib.pyplot.show()
