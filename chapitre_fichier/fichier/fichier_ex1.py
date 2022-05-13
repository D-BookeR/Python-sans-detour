#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Premier exemple de lecture de fichier
sans gestion des erreurs
"""
f = open('/tmp/essai.txt', 'rt')
contenu_fichier = f.read()
print(contenu_fichier)
f.close()
