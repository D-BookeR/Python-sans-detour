import numpy
import PIL.Image
import PIL.ImageDraw
import tensorflow

model = tensorflow.keras.models.load_model('/tmp/esrgan-tf2')
img_orig = PIL.Image.open("/tmp/kite.jpg")
long_carre = min(img_orig.height, img_orig.width)
img_orig = img_orig.crop((0, 0, long_carre, long_carre))
img_orig = img_orig.resize((256, 256))
miniature = img_orig.resize((64, 64))
img = numpy.asarray(miniature)
miniature_x4_dnn = model([img])
img_np = miniature_x4_dnn.numpy()[0, :, :, :]
img_np = numpy.clip(img_np, 0, 255)
img = img_np.astype(numpy.uint8)
img_pil = PIL.Image.fromarray(img)
planche = PIL.Image.new(img_pil.mode,
                        (2 * img_pil.width, 2 * img_pil.height))
planche.paste(miniature, (92, 92))
planche.paste(img_pil, (img_pil.width, 0))
miniature_x4 = miniature.resize((4 * miniature.width, 4 * miniature.height),
                                PIL.Image.LANCZOS)
planche.paste(miniature_x4, (0, img_pil.height))
planche.paste(img_orig, (img_pil.width, img_pil.height))
planche.show()
