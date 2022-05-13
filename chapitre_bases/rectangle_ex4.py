import rectangle_ex1 as rct

x = rct.Rectangle(6, 5)
print("La largeur du rectangle x est de : ", x.largeur)
print("La hauteur du rectangle x est de : ", x.hauteur)
y = rct.Rectangle(rct.Rectangle(4, 5).surface(),
                  rct.Rectangle(6, 5).perimetre())
print("La hauteur du rectangle y est de : ", y.hauteur)
print("La largeur du rectangle y est de : ", y.largeur)