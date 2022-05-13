#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Exemple lecture du classeur complet sans header
"""
import pandas


def afficher_feuille(feuille):
    """
    Affiche chaque cellule d'une feuille extrait d'un classeur excel
    avec une cellule par ligne
    Paramètres
    ----------
    feuille : DataFrame
        feuille du tableur

    valeur de retour
    -----------------
        aucune
    """
    for nom_colonne in feuille:
        for cellule in feuille[nom_colonne]:
            print(cellule)


def afficher_feuille_reference(feuille):
    """
    Affiche chaque cellule d'une feuille avec
    sa référence extrait d'un classeur excel
    avec une cellule par ligne
    Paramètres
    ----------
    feuille : DataFrame
        feuille du tableur

    valeur de retour
    -----------------
        aucune
    """
    for ind_col, nom_colonne in enumerate(feuille):
        for ind_lig, cellule in enumerate(feuille[nom_colonne]):
            reference = "L" + str(ind_lig + 1) + "C" + str(ind_col + 1) + "= "
            print(reference, cellule, '\t')


if __name__ == '__main__':
    nom_classeur = "/tmp/mon_tableur.xlsx"
    classeur = pandas.read_excel(nom_classeur,
                                 sheet_name=None,
                                 header=None)
    print("Le classeur ", nom_classeur,
          " comporte ", len(classeur), " feuilles")
    for nom_feuille in classeur:
        print(50 * "*")
        print("Feuille : ", nom_feuille)
        afficher_feuille_reference(classeur[nom_feuille])
