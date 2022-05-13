import matplotlib.pyplot
import PIL
import PIL.ImageGrab

copie_ecran = PIL.ImageGrab.grab()
copie_ecran.save("/tmp/ecran_copie.png")
fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=1)
ax.imshow(copie_ecran)
ax.set_title("Copie d'écran")
matplotlib.pyplot.show()
