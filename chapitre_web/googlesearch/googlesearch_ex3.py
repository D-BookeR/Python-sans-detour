import sys
import os
import urllib
import googlesearch

resultat = googlesearch.search("filetype:pdf python context manager",
                               num=10,
                               lang="fr",
                               stop=10)
for url_pdf in resultat:
    try:
        with urllib.request.urlopen(url_pdf) as reponse:
            doc_pdf = reponse.read()
    except urllib.error.URLError:
        print(print(sys.exc_info()))
        print("Problème de lecture de l'URL : ", url_pdf)
        doc_pdf = None
    if doc_pdf:
        try:
            nom_fichier = os.path.basename(url_pdf)
            with open('/tmp/' + nom_fichier, "wb") as f:
                f.write(doc_pdf)
        except OSError:
            print(sys.exc_info())
            print("Erreur lors d'écriture de ", nom_fichier)
