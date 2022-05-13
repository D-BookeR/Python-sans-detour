import sys
import os
import urllib
import ssl
import googlesearch

extra_params = {'filetype':'pdf'}
resultat = googlesearch.search("filetype:pdf python context manager",
                               num=10,
                               lang="fr",
                               stop=10)

liste_pdf = [url_pdf for idx,url_pdf in enumerate(resultat)]

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

for url_pdf in liste_pdf:
    try:
        gcontext = ssl.SSLContext()
        page=urllib.request.Request(url_pdf,headers={'User-Agent': 'Mozilla/5.0'}) 
        with urllib.request.urlopen(page) as reponse:
            print("Lecture de l'URL : ", url_pdf)
            page_html = reponse.read()
            nom_fichier = os.path.basename(url_pdf) 
            print("La taille du fichier ",nom_fichier, " est de ", len(page_html))
    except OSError:
        print(print(sys.exc_info()))
        print("Problème de lecture de l'URL : ", url_pdf)
    