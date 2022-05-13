import os
import sys
import urllib.request
import ssl
import zipfile
import certifi
import numpy
import matplotlib.pyplot

contexte_local = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                            cafile=certifi.where())
contexte_local.check_hostname = True
contexte_local.verify_mode = ssl.CERT_REQUIRED

url_site = "https://www.insee.fr/fr/statistiques/series/csv/famille/102775111"
try:
    with urllib.request.urlopen(url_site, context=contexte_local) as response:
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
origine = 0
nb_ligne = 101
titre_courbe = [v.replace('"', '')
                for v in val_csv[origine: origine + nb_ligne, 0]]
titre_courbe = [v[2] for v in numpy.char.split(titre_courbe, ' - ')]
classe = 0
x_homme = val_csv[classe * nb_elt_classe + origine:
                  classe * nb_elt_classe + origine + nb_ligne,
                  4:]
classe = 1
x_femme = val_csv[classe * nb_elt_classe + origine:
                  classe * nb_elt_classe + origine + nb_ligne,
                  4:]
population_hf = numpy.zeros(shape=(nb_ligne, x_annee.shape[0]),
                            dtype=numpy.single)
for ind_ligne in range(nb_ligne):
    nb_h = [numpy.int32(v.replace('"', '')) for v in x_homme[ind_ligne, :]]
    nb_f = [numpy.int32(v.replace('"', '')) for v in x_femme[ind_ligne, :]]
    population_hf[ind_ligne, :] = numpy.array(nb_h) + numpy.array(nb_f)
nb_cellule_h = 10
nb_ligne_graphique = (nb_ligne - 1) // nb_cellule_h + 1
fig, ax = matplotlib.pyplot.subplots(nrows=nb_ligne_graphique,
                                     ncols=nb_cellule_h)
for ind, population in enumerate(population_hf):
    ind_lig, ind_col = divmod(ind, nb_cellule_h)
    ax[ind_lig][ind_col].plot(x_annee, population, label=titre_courbe[ind])
    ax[ind_lig][ind_col].tick_params(axis='both', labelsize=5)
    exposant = ax[ind_lig][ind_col].yaxis.get_offset_text()
    exposant.set_size(5)
    ax[ind_lig][ind_col].legend(loc='lower left', fontsize=5)
for ind in range(nb_ligne, nb_cellule_h * nb_ligne_graphique):
    ind_lig, ind_col = divmod(ind, nb_cellule_h)
    fig.delaxes(ax[ind_lig][ind_col])
matplotlib.pyplot.show()
