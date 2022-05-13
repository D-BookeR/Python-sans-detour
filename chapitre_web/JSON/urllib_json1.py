import sys
import urllib.request
import ssl
import json
import certifi

url_site = "https://wxs.ign.fr/calcul/alti/rest/elevation.json?"
url_site = url_site + "lon=0.2|0.4&lat=48.0|48.1"
contexte_local = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                            cafile=certifi.where())
contexte_local.check_hostname = True
contexte_local.verify_mode = ssl.CERT_REQUIRED

try:
    with urllib.request.urlopen(url_site, context=contexte_local) as response:
        reponse_json = response.read()
except urllib.error.URLError:
    print(sys.exc_info())
    print("Problème de lecture de l'URL : ", url_site)
    sys.exit()
mes_infos = json.loads(reponse_json)
print(mes_infos)
print(mes_infos["elevations"][1]['lon'])
