import sys
import urllib.request

url_page = "https://matplotlib.org/stable/tutorials/introductory/images.html"
try:
    with urllib.request.urlopen(url_page) as reponse:
        page_html = reponse.read()
except urllib.error.URLError:
    print("Une erreur s'est produite lors de l'ouverture de la page")
    print(sys.exc_info())
with open("/tmp//images.html","wb") as f:
    f.write(page_html)
