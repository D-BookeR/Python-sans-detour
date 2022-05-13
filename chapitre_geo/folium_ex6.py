import os
import webbrowser
import folium

carte = folium.Map([46.59, 2.48],
                   zoom_start=10,
                   control_scale=True)
l_icones = [([46.4, 2.3], "fontawesome 4.7", "green", "mixcloud", 'fa'),
            ([46.4, 2.4], "fontawesome 4.7", "green", "space-shuttle", 'fa'),
            ([46.4, 2.5], "fontawesome 4.7", "green", "arrows", 'fa'),
            ([46.5, 2.3], "glyphicons", "red", "camera", 'glyphicon'),
            ([46.5, 2.4], "glyphicons", "red", "book", 'glyphicon'),
            ([46.5, 2.5], "glyphicons", "red", "signal", 'glyphicon'),
            ]
for p_marqueur in l_icones:
    marqueur = folium.Marker(p_marqueur[0],
                             popup=p_marqueur[1],
                             icon=folium.Icon(color=p_marqueur[2],
                                              icon=p_marqueur[3],
                                              prefix=p_marqueur[4]))
    marqueur.add_to(carte)
chemin_fichier = os.path.splitdrive(os.getcwd())[0] + \
                 "/tmp/ma_carte_centre.html"
carte.save(chemin_fichier)
webbrowser.open("file:///" + chemin_fichier)
