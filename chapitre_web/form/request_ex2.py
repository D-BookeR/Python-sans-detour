import os
import webbrowser
import sys
import requests

url_site = "https://www.traimaocv.fr/affiche_header.php"
ma_session = requests.Session()
try:
    page = ma_session.post(url_site)
except requests.exceptions.RequestException:
    print("Erreur : ", sys.exc_info())
    sys.exit()
if page.status_code != requests.codes['ok']:
    print("page non lue : ", page.status_code)
    sys.exit()
with open("/tmp/header.html","w", encoding=page.encoding) as f:
    f.write(page.text)
nom = 'file://' + os.path.splitdrive(os.getcwd())[0] +'/tmp/header.html'
webbrowser.open(nom)