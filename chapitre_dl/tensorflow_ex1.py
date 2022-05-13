import json
import numpy
import PIL.Image
import PIL.ImageDraw
import tensorflow

modele = tensorflow.keras.models.load_model('/tmp/faster_rcnn_resnet101')
img_orig = PIL.Image.open("/tmp/kites_surf_bis.jpg")
try:
    with open('/tmp/coco_90.json') as f:
        contenu = f.read()
        nom_classe = json.loads(contenu)
except OSError:
    nom_classe = None
    print("Le fichier /tmp/coco_90.json n'a pas été trouvé.")
img_np = numpy.asarray(img_orig)
resultat = modele([img_np])
img_res = img_orig.convert("RGBA")
graphique = PIL.ImageDraw.Draw(img_res)
nb_detections = resultat['num_detections'].numpy()[0].astype(numpy.int32)
for idx in range(nb_detections):
    if resultat['detection_scores'][0, idx].numpy() > 0.5:
        rect = (resultat['detection_boxes'].numpy()[0, idx, :])
        rect = tuple([int(rect[1] * img_orig.width),
                      int(rect[0] * img_orig.height),
                      int(rect[3] * img_orig.width),
                      int(rect[2] * img_orig.height)])
        graphique.rectangle(rect, outline='red')
        idx_classe = str(int(resultat['detection_classes'][0, idx].numpy()))
        if nom_classe:
            nom = nom_classe[idx_classe]['name']
        else:
            nom = str(idx_classe)
        graphique.text(rect[0:2], nom, fill=(0, 0, 0))
        graphique.text(rect[2:4], nom, fill=(255, 255, 255))
img_res.show()
