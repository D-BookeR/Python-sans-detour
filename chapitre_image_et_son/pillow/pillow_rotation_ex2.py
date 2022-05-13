import numpy
import matplotlib.pyplot
import PIL

img = PIL.Image.open("/tmp/baboon.jpg")
largeur, hauteur = img.width, img.height
larg_x2 = int(numpy.sqrt(largeur ** 2 + hauteur ** 2)) + 1
img_x2 = PIL.Image.new(img.mode, (larg_x2, larg_x2))
img_x2.paste(img, (larg_x2 // 2 - largeur // 2, larg_x2 // 2 - hauteur // 2))
l_angle = [45, 90, 135]
l_image = [img_x2.rotate(v) for v in l_angle]
l_angle.insert(0, 0)
l_image.insert(0, img_x2)
fig, ax = matplotlib.pyplot.subplots(nrows=2, ncols=2)
for idx, img in enumerate(l_image):
    idx_lig, idx_col = idx // 2, idx % 2
    ax[idx_lig][idx_col].imshow(img)
    ax[idx_lig][idx_col].set_title("rotation " + str(l_angle[idx]))
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
