#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Quatrième exemple de écriture de fichier
avec gestion des erreurs
"""
try:
    mon_contenu = "Tout augmente 110€\ncaractères UTF-8 ☁"
    with open('/tmp/mon_fichier.txt', 'wt', encoding='UTF-8') as f:
        f.write(mon_contenu)
except OSError:
    print("Le fichier n'a pas pu être ouvert, vérifiez le chemin")
except UnicodeDecodeError:
    print("l'encodage utilisé ne correspond pas aux données du fichier")
