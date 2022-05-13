import os
import sys
import webbrowser
import requests
import folium
import geopy.geocoders


localiseur = geopy.geocoders.Nominatim(user_agent="python_dbooker")
adr_deb, (lat_deb, lon_deb) = localiseur.geocode("Saint léonard des bois")
adr_fin, (lat_fin, lon_fin) = localiseur.geocode("Saint Céneri")
url_base = """
https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0\
/route?resource=bdtopo-pgr&profile=pedestrian"""
url_iti = "&start=" + str(lon_deb) + "," + str(lat_deb)
url_iti += "&end=" + str(lon_fin) + "," + str(lat_fin)
url_param = "&geometryFormat=geojson&getSteps=true&waysAttributes=cleabs"
print(url_base + url_iti + url_param)
ma_session = requests.Session()
try:
    reponse = ma_session.get(url_base + url_iti + url_param)
    if reponse.status_code != requests.codes.ok:
        print("page non lue : ", reponse.status_code)
        sys.exit()
except requests.exceptions.RequestException:
    print("Erreur : ", sys.exc_info())
    sys.exit()
itineraire = reponse.json()
lat_centre = (lat_deb + lat_fin) / 2
lon_centre = (lon_deb + lon_fin) / 2
carte = folium.Map([lat_centre, lon_fin],
                   zoom_start=14,
                   control_scale=True)
tps_parcours, km_parcours = 0, 0
l_etapes = itineraire["portions"][0]["steps"]
etape_pre = l_etapes[0]["geometry"]["coordinates"][0][::-1]
for etape in l_etapes:
    ins_marqueur = True
    for lon_lat in etape["geometry"]["coordinates"]:
        ligne = folium.ColorLine([etape_pre, lon_lat[::-1]],
                                 [1],
                                 colormap=['blue', 'green'],
                                 weight=4)
        carte.add_child(ligne)
        if ins_marqueur:
            tps_parcours = tps_parcours + etape["duration"]
            km_parcours = km_parcours + etape["distance"]
            texte = str(int(tps_parcours)) + " min. / " +\
                    str(km_parcours) + "m" +\
                    etape["attributes"]["nom_1_gauche"]
            marqueur = folium.Marker(lon_lat[::-1],
                                     popup=texte,
                                     icon=folium.Icon(color='red'))
            marqueur.add_to(carte)
            ins_marqueur = False
        etape_pre = lon_lat[::-1]
chemin_fichier = os.path.splitdrive(os.getcwd())[0] + \
                 "/tmp/ma_carte_rando.html"
carte.save(chemin_fichier)
webbrowser.open("file:///" + chemin_fichier)
