import numpy
import cv2
import tensorflow
import wx

app = wx.App()
nom_style = wx.FileSelector('Image Style', wildcard="Image (*.jpg)|*.jpg")
del app
modele_style = tensorflow.keras.models.load_model("/tmp/neural_style")
img_style = cv2.imread(nom_style, cv2.IMREAD_COLOR)
img_style = cv2.resize(img_style, (256, 256))
x_styl = numpy.array([(numpy.asarray(img_style) / 256).astype(numpy.float32)])
modele_objet = tensorflow.keras.models.load_model('/tmp/faster_rcnn_resnet101')
video = cv2.VideoCapture('/tmp/vtest.avi')
while video.isOpened():
    lecture_ok, img_np = video.read()
    if lecture_ok:
        res = modele_objet([img_np])
        nb_detections = res['num_detections'].numpy()[0].astype(numpy.int32)
        for idx in range(nb_detections):
            if res['detection_scores'][0, idx].numpy() > 0.5 and\
               res['detection_classes'][0, idx].numpy() == 1:
                rect = (res['detection_boxes'].numpy()[0, idx, :])
                rect = tuple([int(rect[1] * img_np.shape[1]),
                              int(rect[0] * img_np.shape[0]),
                              int(rect[3] * img_np.shape[1]),
                              int(rect[2] * img_np.shape[0])])
                ext_lig = slice(rect[1], rect[3])
                ext_col = slice(rect[0], rect[2])
                img_personne = numpy.array([img_np[ext_lig, ext_col] / 256],
                                           dtype=numpy.float32)
                resultat = modele_style(tensorflow.constant(img_personne),
                                        tensorflow.constant(x_styl))
                humain_style = (resultat[0].numpy()[0]*256).astype(numpy.uint8)

                img_np[ext_lig, ext_col] = \
                    humain_style[0:rect[3]-rect[1], 0:rect[2]-rect[0]]
        cv2.imshow("video", img_np)
        touche = cv2.pollKey()
        if touche == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()
