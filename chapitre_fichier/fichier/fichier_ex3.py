#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Troisième exemple de lecture de fichier
avec gestion des erreurs
"""
try:
    with open('/tmp/essai.txt', 'rt', encoding='UTF-8') as f:
        contenu_fichier = f.read()
        print(contenu_fichier)
except OSError:
    print("Le fichier n'a pas pu être ouvert, vérifiez le chemin")
except UnicodeDecodeError:
    print("L'encodage utilisé ne correspond pas aux données du fichier")
