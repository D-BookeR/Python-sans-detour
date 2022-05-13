import rectangle_ex1

x = rectangle_ex1.Rectangle(6, 5)
print("La largeur du rectangle x est de : ", x.largeur)
print("La hauteur du rectangle x est de : ", x.hauteur)
y = rectangle_ex1.Rectangle(rectangle_ex1.Rectangle(4, 5).surface(),
                            rectangle_ex1.Rectangle(6, 5).perimetre())
print("La hauteur du rectangle y est de : ", y.hauteur)
print("La largeur du rectangle y est de : ", y.largeur)