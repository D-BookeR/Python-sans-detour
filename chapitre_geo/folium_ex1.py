import os
import webbrowser
import folium

carte = folium.Map([46.763, 2.425])
chemin_fichier = os.path.splitdrive(os.getcwd())[0] + "/tmp/ma_carte.html"
carte.save(chemin_fichier)
webbrowser.open("file://" + chemin_fichier)
