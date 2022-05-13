#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Exemple lecture du classeur complet sans header
"""
import doctest
import math
import pandas


def lettre_colonne(ind_colonne):
    """
    converti un numéro de colonne de tableur en référence sous forme de lettre
    Paramètres
    ----------
    ind_colonne : int
        indice de la colone dont on cherche la référence en lettre
    valeur de retour
    -----------------
        str égal à la référence de la colonne
    tests unitaires
    ---------------
    >>> lettre_colonne(1)
    'A'
    >>> lettre_colonne(256)
    'IV'
    >>> lettre_colonne(16384)
    'XFD'
    """
    if not isinstance(ind_colonne, int):
        raise TypeError("ind_colonne doit être du type int")
    if ind_colonne < 1:
        raise ValueError("ind_colonne doit être du supérieur ou égal à 1")
    ref_colonne = []
    while ind_colonne != 0:
        ref_colonne.append(chr(ind_colonne % 26 + 64))
        ind_colonne = ind_colonne // 26
    return ''.join(ref_colonne[::-1])


def afficher_feuille_reference(feuille, reference_lc=True):
    """
    Affiche chaque cellule d'une feuille avec
    sa référence extrait d'un classeur excel
    avec une cellule par ligne
    Paramètres
    ----------
    feuille : DataFrame
        feuille du tableur
    reference_lc : bool
        true pour un affichage L1C1 sinon affichage A1
    valeur de retour
    -----------------
        aucune
    """
    for ind_col, nom_colonne in enumerate(feuille):
        for ind_lig, cellule in enumerate(feuille[nom_colonne]):
            if reference_lc:
                reference = "L" + str(ind_lig + 1) + "C" +\
                            str(ind_col + 1) + "= "
            else:
                reference = lettre_colonne(ind_col + 1) + str(ind_lig + 1)
            if cellule == cellule:
                print(reference, cellule, '\t')


if __name__ == '__main__':
    doctest.testmod()
    nom_classeur = "/tmp/mon_tableur.xlsx"
    classeur = pandas.read_excel(nom_classeur,
                                 sheet_name=None,
                                 header=None)
    print("Le classeur ", nom_classeur,
          " comporte ", len(classeur), " feuilles")
    for nom_feuille in classeur:
        print(50 * "*")
        print("Feuille : ", nom_feuille)
        afficher_feuille_reference(classeur[nom_feuille], False)
