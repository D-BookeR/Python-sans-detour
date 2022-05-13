import os
import webbrowser
import folium
import geopy.geocoders

centres_france = [
    ((46, 45, 47), (2, 25, 29)),
    ((46, 45, 34), (2, 24,  4)),
    ((46, 43, 17), (2, 30, 37)),
    ((46, 36, 21), (2, 29, 54)),
    ((46, 32, 23), (2, 25, 49)),
    ((46, 29,  1), (2, 31, 35)),
    ((46, 22, 26), (2, 28, 39)),
    ((46, 29, 38), (2, 36, 10))
    ]
carte = folium.Map([46.59, 2.48],
                   zoom_start=10,
                   control_scale=True)
localiseur = geopy.geocoders.Nominatim(user_agent="python_dbooker")
for c_france in centres_france:
    lat_centre = geopy.Point.parse_degrees(c_france[0][0],
                                           c_france[0][1],
                                           c_france[0][2]
                                           )
    lon_centre = geopy.Point.parse_degrees(c_france[1][0],
                                           c_france[1][1],
                                           c_france[1][2]
                                           )
    lieu = localiseur.reverse(str(lat_centre)+","+str(lon_centre))
    texte = "<b>" + lieu.address + "</b>"
    folium.Marker([lat_centre, lon_centre], popup=texte).add_to(carte)
chemin_fichier = os.path.splitdrive(os.getcwd())[0] + \
                 "/tmp/ma_carte_centre.html"
carte.save(chemin_fichier)
webbrowser.open("file:///" + chemin_fichier)
