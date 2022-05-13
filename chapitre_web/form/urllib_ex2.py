import os
import urllib.request
import webbrowser

reponse_post = urllib.request.Request(
    "https://www.traimaocv.fr/affiche_header.php",
    method='POST')
with urllib.request.urlopen(reponse_post) as lien_page:
    page = lien_page.read().decode('utf-8')
with open("/tmp/header.html", "w", encoding='utf-8') as f:
    f.write(page)
nom = 'file://' + os.path.splitdrive(os.getcwd())[0] +\
    '/tmp/header.html'
print(nom)
webbrowser.open(nom)
