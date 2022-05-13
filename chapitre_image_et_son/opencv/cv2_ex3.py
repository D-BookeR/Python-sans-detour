import time
import sys
import cv2

flux_entree = cv2.VideoCapture(0, cv2.CAP_ANY)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = 15
flux_sortie = cv2.VideoWriter('/tmp/output.avi', fourcc, fps, (640,  480))
if not flux_entree.isOpened():
    print("Le flux d'entrée ne peut être ouvert")
    sys.exit()
if not flux_sortie.isOpened():
    print("Le flux de sortie ne peut être ouvert")
    flux_entree.release()
    sys.exit()
tps_img_sui = time.time_ns() + 1 / fps * 1e9
while True:
    ret, img = flux_entree.read()
    if not ret:
        print("erreur ou fin de la lecture du flux")
        break
    tps_attente = tps_img_sui - time.time_ns()
    if tps_attente > 0:
        time.sleep(tps_attente * 1e-9)
    else:
        print("FPS trop grand")
    tps_img_sui += 1 / fps * 1e9
    flux_sortie.write(img)
    cv2.imshow('Webcam', img)
    if cv2.pollKey() == ord('q'):
        break
flux_entree.release()
flux_sortie.release()
cv2.destroyAllWindows()
