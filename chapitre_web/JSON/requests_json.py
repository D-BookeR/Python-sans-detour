import sys
import json
import requests

url_site = "https://wxs.ign.fr/calcul/alti/rest/elevation.json?"
url_site = url_site + "lon=0.2|0.4&lat=48.0|48.1"
ma_session = requests.Session()
try:
    reponse = ma_session.get(url_site)
    if reponse.status_code != requests.codes.ok:
        print("page non lue : ", reponse.status_code)
        sys.exit()
except requests.exceptions.RequestException:
    print("Erreur : ", sys.exc_info()) 
    sys.exit()
mes_infos = json.loads(reponse.content)
print(mes_infos)
print(mes_infos["elevations"][0]['lon'])
