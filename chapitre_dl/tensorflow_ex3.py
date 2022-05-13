import numpy
import PIL.Image
import PIL.ImageDraw
import tensorflow

model = tensorflow.keras.models.\
        load_model(r"/tmp/neuralstyle")
img_orig = PIL.Image.open("/tmp/style_bonhomme.jpg")
img_style = PIL.Image.\
            open("/tmp/baboon.jpg")
img_style = img_style.resize((256, 256))
img = img_orig
x_orig = numpy.array([(numpy.asarray(img_orig) / 256).astype(numpy.float32)])
x_styl = numpy.array([(numpy.asarray(img_style) / 256).astype(numpy.float32)])
resultat = model(tensorflow.constant(x_orig), tensorflow.constant(x_styl))
img_tr = resultat[0].numpy()[0]
img = PIL.Image.fromarray((img_tr*256).astype(numpy.uint8))
img.show()
