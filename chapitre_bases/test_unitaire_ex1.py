#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Exemple de programme avec test unitaire
"""

import doctest


def produit_divise(para):
    """
    produit_divise effectue le produit du nombre par 2
    si le nombre est compris entre 0 et 1 sinon le nombre est divisé par 2
    Paramètres
    ----------
    para : type numérique
        nombre à traiter par la fonction

    valeurs de retour
    -----------------
        si para est compris entre 0 et 1 2para sinon para/2
    tests unitaires
    ---------------
    >>> produit_divise(0.5)
    1.0
    >>> produit_divise(4)
    2.0
    >>> produit_divise(5.0)
    2.5
    """
    if 0 <= para <= 1:
        resu = 22 * para
    else:
        resu = para / 2
    return resu

if __name__ == '__main__':
    doctest.testmod()
    print("Fin du programme")
 