#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ce programme compresse les fichiers contenus dans un dossier
dont la taille est supérieure au choix de l'utilisateur et
crée un classeur excel avec deux feuilles
la première avec les chemins complets de fichiers avec leur taille
et la date de modification du fichier
la seconde feuille avec le cemin complet des fichiers et
leur taille
"""
import os
import datetime
import zipfile
import pandas


def explore_dossier(dossier):
    """
    Création de deux listes contenant tous
    les fichiers d'un répertoire et sous répertoire
    avec leur taille et la date de création du fichier
    Paramètre
    ----------
    nom_dossier : chemin complet du dossier

    valeur de retour
    -----------------
    liste des chemins complets des fichiers avec
    leurs tailles en octet
    liste des chemins complets de l'ensemble des répertoires avec
    la taille de ses dossiers
    """
    liste_fichiers = []
    liste_dossiers = []
    taille_dossier = 0
    sec_vers_date = datetime.datetime.fromtimestamp
    with os.scandir(dossier) as list_entree:
        for entree in list_entree:
            if entree.is_file():
                date_modif = sec_vers_date(entree.stat().st_mtime)
                liste_fichiers.append([entree.path,
                                       entree.stat().st_size,
                                       date_modif])
                taille_dossier = taille_dossier + entree.stat().st_size
            elif entree.is_dir(follow_symlinks=False):
                l_fichier, l_dossier = explore_dossier(entree.path)
                liste_fichiers = liste_fichiers + l_fichier
                liste_dossiers = liste_dossiers + l_dossier
        liste_dossiers.append([dossier, taille_dossier])
    return liste_fichiers, liste_dossiers


def compresser_fichiers(liste_fichiers, nom_archive):
    """
    Création d'une archive
    contenat tous les fichiers dont les chemins complets sont
    dans la liste liste_fichiers
    Paramètre
    ----------
    liste_fichiers : list chemin complet des fichiers à archiver
    nom_archive : chemin complet de l'archive à créer

    valeur de retour
    -----------------
    Aucune
    """
    with zipfile.ZipFile(nom_archive, 'a') as zip:
        for nom_fichier in liste_fichiers:
            zip.write(nom_fichier, os.path.abspath(nom_fichier))


def selection_fichier(liste_fichiers, taille_minimum=16384, date_minimum=None):
    """
    Sélection des fichiers dans une liste
    Différents critères sont possible :
        * selon la taille en octet du fichier lorsque
          taille_minimum est non nul et date_minimum=None
        * selon la date lorsque date_minimum est défini
          et taille_minimum est None et date_minimum=None
        * selon la date et la talle lorsque
          les deux paramètres sont définis
    La taille est en octet et
    date_minimum est un objet par exemple
    datetime.datetime(2021, 6, 20,19, 40) pour le 20 juin 2021 à 19h40
    la liste des fichiers est une list d'éléments de type list. Chaque
    élement de type list est composé de trois éléments, le chemin
    complet du fichier, la taille en octet et
    la date de dernière modification (objet datetime.datetime)

    Paramètres
    ----------
    liste_fichiers : liste des fichiers à sélectionner
    taille_minimum : int taille minimale des fichiers à sélectionner
    date_minimum : objet de type datetime.datetime

    valeur de retour
    -----------------
    liste des chemins complets vérifiant les critères
    """
    selection_fichiers = []
    if date_minimum is None:
        for ligne_fichier in liste_fichiers:
            if ligne_fichier[1] > taille_minimum:
                selection_fichiers.append(ligne_fichier[0])
    elif taille_minimum is None:
        for ligne_fichier in liste_fichiers:
            if ligne_fichier[2] > date_minimum:
                selection_fichiers.append(ligne_fichier[0])
    else:
        for ligne_fichier in liste_fichiers:
            if ligne_fichier[1] > taille_minimum and\
               ligne_fichier[2] > date_minimum:
                selection_fichiers.append(ligne_fichier[0])
    return selection_fichiers


def creer_classeur(nom_classeur, dossier, liste_fichiers, liste_dossiers):
    """
    Création d'un classeur Excel nommé nom_classeur
    avec deux feuilles, le premier nommé nom_dossier et le second
    "taille des dossiers".
    La première feuille contient en colonne A le chemin complet du fichier,
    en colonne B sa taille en octet et en colonne C sa date de dernière
    modification.
    La seconde feuille contient en colonne A le nom du répertoire
    et en colonne B la taille totale des fichiers du répertoire.

    Paramètres
    ----------
    liste_fichiers : type list liste des fichiers à sélectionner
    taille_minimum : int taille minimale des fichiers à sélectionner
    date_minimum : objet de type datetime.datetime

    valeur de retour
    -----------------
        aucune
    """
    feuille1 = pandas.DataFrame(liste_fichiers)
    feuille2 = pandas.DataFrame(liste_dossiers)
    with pandas.ExcelWriter(nom_classeur) as classeur_doc:
        feuille1.to_excel(classeur_doc,
                          sheet_name=dossier,
                          index=False,
                          header=False)
        feuille2.to_excel(classeur_doc,
                          sheet_name="Taille des dossiers",
                          index=False,
                          header=False)


def creer_csv(nom_classeur, liste_fichiers):
    feuille = pandas.DataFrame(liste_fichiers)
    feuille.to_csv(nom_classeur, index=False, header=False)
    feuille.to_clipboard(index=False, header=False)


if __name__ == '__main__':
    nom_dossier = '/tmp/opencv'
    l_fichiers, l_dossiers = explore_dossier(nom_dossier)
    creer_classeur("mon_dossier.xlsx",
                   "opencv",
                   l_fichiers,
                   l_dossiers)
    creer_csv("mon_dossier.csv", l_fichiers)
    selection = selection_fichier(l_fichiers, 2 ** 25)
    if len(selection) > 0:
        compresser_fichiers(selection, "/tmp/mon_archive.zip")
