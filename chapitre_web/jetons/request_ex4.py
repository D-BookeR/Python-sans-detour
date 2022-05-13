import os
import webbrowser
import requests

url_site = "https://exemple.traimaocv.fr/index/frequence"
ma_session = requests.Session()
requete_post = dict(
    freq='1.23',
    phase='4.56',
    )
page = ma_session.post(url_site, data=requete_post)
with open("/tmp/frequence.html", "w", encoding=page.encoding) as f:
    f.write(page.text)
nom = 'file://' + os.path.splitdrive(os.getcwd())[0] + '/tmp/frequence.html'
webbrowser.open(nom)
