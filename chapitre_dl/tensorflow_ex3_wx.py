import numpy
import PIL.Image
import PIL.ImageDraw
import tensorflow
import wx

app = wx.App()
nom_style = wx.FileSelector('Image Style', wildcard="Image (*.jpg)|*.jpg")
nom_image = wx.FileSelector('Image', wildcard="Image (*.jpg)|*.jpg")
del app
model = tensorflow.keras.models.load_model("/tmp/neural_style")
img_orig = PIL.Image.open(nom_image)
img_style = PIL.Image.open(nom_style)
img_style = img_style.resize((256, 256))
x_orig = numpy.array([(numpy.asarray(img_orig) / 256).astype(numpy.float32)])
x_styl = numpy.array([(numpy.asarray(img_style) / 256).astype(numpy.float32)])
resultat = model(tensorflow.constant(x_orig), tensorflow.constant(x_styl))
img_modifie = resultat[0].numpy()[0]
img = PIL.Image.fromarray((img_modifie * 256).astype(numpy.uint8))
img.show()
