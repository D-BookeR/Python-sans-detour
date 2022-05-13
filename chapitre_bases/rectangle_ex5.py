from rectangle_ex1 import Rectangle

x = Rectangle(6, 5)
print("La largeur du rectangle x est de : ", x.largeur)
print("La hauteur du rectangle x est de : ", x.hauteur)
y = Rectangle(Rectangle(4, 5).surface(),
              Rectangle(6, 5).perimetre())
print("La hauteur du rectangle y est de : ", y.hauteur)
print("La largeur du rectangle y est de : ", y.largeur)
