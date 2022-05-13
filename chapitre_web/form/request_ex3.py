import os
import webbrowser
import sys
import requests

url_site = "https://www.traimaocv.fr/affiche_header.php"
ma_session = requests.Session()
entete = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "referer":
    "https://exemple.traimaocv.fr/index"}
try:
    page = ma_session.post(url_site, headers=entete)
except requests.exceptions.RequestException:
    print("Erreur : ", sys.exc_info())
    sys.exit()
if page.status_code != requests.codes['ok']:
    print("page non lue : ", page.status_code)
    sys.exit()
with open("/tmp/header.html", "w", encoding='utf-8') as f:
    f.write(page.text)
nom = 'file://' + os.path.splitdrive(os.getcwd())[0] + '/tmp/header.html'
webbrowser.open(nom)
