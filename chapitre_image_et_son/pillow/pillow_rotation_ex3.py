import numpy
import matplotlib.pyplot
import PIL

img = PIL.Image.open("/tmp/baboon.jpg")
largeur, hauteur = img.width, img.height
larg_x2 = int(numpy.sqrt(largeur ** 2 + hauteur ** 2)) + 1
img_x2 = PIL.Image.new(img.mode, (larg_x2, larg_x2))
img_x2.paste(img, (larg_x2 // 2 - largeur // 2, larg_x2 // 2 - hauteur // 2))
planche = PIL.Image.new(img.mode, (2 * larg_x2, 2 * larg_x2))
angle = [0, 45, 90, 135]
for idx, v in enumerate(angle):
    idx_lig, idx_col = idx // 2, idx % 2
    origine = (idx_col * larg_x2, idx_lig * larg_x2)
    planche.paste(img_x2.rotate(v), origine)
fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=1)
ax.imshow(planche)
ax.set_title("rotation ")
matplotlib.pyplot.show()
