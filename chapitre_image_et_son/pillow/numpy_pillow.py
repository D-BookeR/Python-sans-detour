import numpy
import matplotlib.pyplot
import PIL.Image


img = PIL.Image.open("/tmp/baboon.jpg")
img_np = numpy.array(img)
print(img_np.shape)
pixel_rouge = numpy.logical_and(img_np[:, :, 0] > 192,
                                img_np[:, :, 1] < 128,
                                img_np[:, :, 2] < 128)
img_np[pixel_rouge, :] = 0
fig, ax = matplotlib.pyplot.subplots(1, 1)
ax.imshow(img_np)
matplotlib.pyplot.show()
np_pillow = PIL.Image.fromarray(img_np)
np_pillow.save("/tmp/numpy_img.jpg")
