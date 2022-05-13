#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mon premier programme
Ce docstring
décrit le module ou le code source
"""

import time

MON_PROGRAME_INDEX = 1

def ma_fonction_bis(para1, para2=3, para3=5):
    """
    ma fonction_bis a trois paramètres et retourne 4 résultats
    correspondants à la somme deux à deux des paramètres
    Paramètres
    ----------
    para1 : type
        première valeur
    para2 : type
        deuxième valeur, par défaut égal à 3
    para3 :
        troisième valeur, par défaut égal à 5

    valeurs de retour
    -----------------
        la somme du premier avec le deuxième,
        la somme du premier avec le troisième,
        la somme du deuxième avec le troisième,
        la somme des trois paramètres

    note
    ----
    type peut être numérique (int ou float) ou bien str. Si le type str est choisi,
    les trois paramètres doivent etre str
    """
    s_12 = para1 + para2
    s_13 = para1 + para3
    s_23 = para2 + para3
    s_123 = para1 + para2 + para3
    return s_12, s_13, s_23, s_123

if __name__ == '__main__':
    print(time.asctime())
    help(ma_fonction_bis)
    val_par = 7, 4, 8
    print("ma_fonction_bis ", val_par, " = ",
        ma_fonction_bis(val_par[0], val_par[1], val_par[2]))
    input("appuyez sur entrée pour terminer")
