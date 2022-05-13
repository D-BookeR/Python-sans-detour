import sys
import requests

url_site = "https://www.traimaocv.fr/action_page.php"
ma_session = requests.Session()
requete_post = dict(
    var_nom='Hugo',
    var_prenom='Victor'
    )
try:
    page = ma_session.post(url_site, data=requete_post)
except requests.exceptions.RequestException:
    print("Erreur : ", sys.exc_info())
    sys.exit()
if page.status_code != requests.codes['ok']:
    print("page non lue : ", page.status_code)
    sys.exit()
print(page.text)
