"""
Classe rectangle
"""


class Rectangle:
    """
    Classe Rectangle définit par  sa largeur et sa hauteur
    """
    def __init__(self, val_largeur, val_hauteur):
        """
        définition du rectangle à partir
        de sa largeur et de sa hauteur
        Argument:
        largeur -- abscisse du centre
        hauteur -- ordonnée du centre
        """
        self.largeur = val_largeur
        self.hauteur = val_hauteur

    def surface(self):
        """
        Calcul de la surface du rectangle
        return : surface du rectangle
        """
        return self.largeur * self.hauteur

    def perimetre(self):
        """
        Calcul du périmètre du rectangle
        return : périmètre du rectangle
        """
        return 2 * (self.largeur + self.hauteur)

    def etirer(self, echelle=1):
        """
        Créer un nouveau rectangle dont les dimensions sont multipliées
        par une constante
        retour : Rectangle
        """
        largeur = echelle * self.largeur
        hauteur = echelle * self.hauteur
        return Rectangle(largeur, hauteur)

    def __call__(self, echelle=1):
        """
        Créer un nouveau rectangle dont les dimensions sont multipliées
        par une constante
        retour : Rectangle
        """
        largeur = echelle * self.largeur
        hauteur = echelle * self.hauteur
        return Rectangle(largeur, hauteur)


if __name__ == "__main__":
    x = Rectangle(5, 4)
    print("La largeur du rectangle est de : ", x.largeur)
    print("La hauteur du rectangle est de : ", x.hauteur)
    print("La surface du rectangle est de : ", x.surface())
    grd_x = x.etirer(2)
    print("La largeur du grand rectangle est de : ", grd_x.largeur)
    print("La hauteur du rectangle est de : ", grd_x.hauteur)
    grd_x = x(3)
    print("La largeur du grand rectangle est de : ", grd_x.largeur)
    print("La hauteur du rectangle est de : ", grd_x.hauteur)
