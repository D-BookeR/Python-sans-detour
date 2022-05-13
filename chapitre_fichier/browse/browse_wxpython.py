import wx

mon_application = wx.App()
nom_classeur = wx.FileSelector(
        'Choisir un fichier',
        wildcard="Classeur (*.xlsx)|*.xlsx")
del mon_application
if len(nom_classeur) != 0:
    print("Chemin complet du fichier : ", nom_classeur)
else:
    print("L'utilisateur a cliqué dans annuler")
