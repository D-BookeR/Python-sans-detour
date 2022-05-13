import os
import webbrowser
import folium


tuile = """
https://server.arcgisonline.com/ArcGIS/rest/services/
World_Imagery/MapServer/tile/{z}/{y}/{x}
"""
credit = """
Tiles &copy; Esri &mdash;
Source: Esri, i-cubed USDA, USGS, AEX, GeoEye, 
Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community
"""
carte_sat = folium.Map([46.763, 2.425],
                       tiles=tuile,
                       attr=credit,
                       zoom_start=15,
                       control_scale=True)
chemin_fichier = os.path.splitdrive(os.getcwd())[0] + \
                 "/tmp/ma_carte_sat.html"
carte_sat.save(chemin_fichier)
webbrowser.open("file:///" + chemin_fichier)
