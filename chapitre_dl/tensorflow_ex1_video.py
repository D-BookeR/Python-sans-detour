import sys
import json
import numpy
import cv2
import tensorflow

modele = tensorflow.keras.models.load_model('/tmp/faster_rcnn_resnet101')
try:
    with open('/tmp/coco_90.json', encoding='utf-8') as f:
        contenu = f.read()
        nom_classe = json.loads(contenu)
except OSError:
    nom_classe = None
    print("Le fichier /tmp/coco_90.json n'a pas été trouvé.")
video = cv2.VideoCapture('/tmp/vtest.avi')
if not video.isOpened():
    print("La vidéo ne peut être ouverte")
    sys.exit()
while True:
    lecture_ok, img_np = video.read()
    if lecture_ok:
        res = modele([img_np])
        nb_detections = res['num_detections'].numpy()[0].astype(numpy.int32)
        for idx in range(nb_detections):
            if res['detection_scores'][0, idx].numpy() > 0.5:
                rect = (res['detection_boxes'].numpy()[0, idx, :])
                rect = tuple([int(rect[1] * img_np.shape[1]),
                              int(rect[0] * img_np.shape[0]),
                              int(rect[3] * img_np.shape[1]),
                              int(rect[2] * img_np.shape[0])])
                cv2.rectangle(img_np, rect[0:2], rect[2:4], (0, 0, 255))
                idx_classe = str(int(res['detection_classes'][0, idx].numpy()))
                if nom_classe:
                    nom = nom_classe[idx_classe]['name']
                else:
                    nom = str(idx_classe)
                cv2.putText(img_np, nom, rect[0:2],
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0))
                cv2.putText(img_np, nom, rect[2:4],
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
        cv2.imshow("video", img_np)
        touche = cv2.pollKey()
        if touche == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()
