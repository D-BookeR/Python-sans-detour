import matplotlib.pyplot
import PIL
import PIL.ImageGrab

img = PIL.Image.open("/tmp/baboon.jpg")
centre = (img.width // 2, img. height // 2)
img45 = img.rotate(45, center=centre)
img90 = img.rotate(90, center=centre)
img135 = img.rotate(135, center=centre)
fig, ax = matplotlib.pyplot.subplots(nrows=2, ncols=2)
ax[0][0].imshow(img)
ax[0][0].set_title("original")
ax[0][1].imshow(img45)
ax[0][1].set_title("rotation 45°")
ax[1][0].imshow(img90)
ax[1][0].set_title("rotation 90°")
ax[1][1].imshow(img135)
ax[1][1].set_title("rotation 135°")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
