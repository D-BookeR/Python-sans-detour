import os
import webbrowser
import requests

url_site = "https://exemple.traimaocv.fr/index/frequence"
ma_session = requests.Session()
entete = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0)" +
    "Gecko/20100101 Firefox/90.0",
    "referer": "https://exemple.traimaocv.fr/index/frequence"}
page = ma_session.get(url_site)

valeur_csrf = ma_session.cookies['csrftoken']
requete_post = dict(
    csrfmiddlewaretoken=valeur_csrf,
    freq='1.23',
    phase='4.56',
    )
page = ma_session.post(url_site, data=requete_post, headers=entete)
with open("/tmp/frequence.html", "w", encoding=page.encoding) as f:
    f.write(page.text)
nom = 'file://' + os.path.splitdrive(os.getcwd())[0] + '/tmp/frequence.html'
webbrowser.open(nom)
