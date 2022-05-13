#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Second exemple de lecture de fichier
avec gestion des erreurs
"""

try:
    f = open('/tmp/essai.txt', "rt")
    contenu_fichier = f.read()
    f.close()
    print(contenu_fichier)
except OSError:
    print("Le fichier n'a pas pu être ouvert. ")
    print("Vérifiez que le chemin est correct ou ")
    print("qu'il n'est pas déjà ouvert")
except UnicodeDecodeError:
    print("l'encodage ne correspond pas aux données du fichier")
