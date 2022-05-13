import sys
import time
import cv2

url = "https://gieat.viewsurf.com/?id=5576&action=mediaRedirect"
flux = cv2.VideoCapture(url)
if not flux.isOpened():
    print("Le flux ne peut être ouvert")
    sys.exit()
fps = flux.get(cv2.CAP_PROP_FPS)
print("Nombre d'images par seconde :", fps)
if fps == 0:
    print("Valeur de FPS nulle.")
    sys.exit()
tps_img_sui = time.time_ns() + 1 / fps * 1e9
while True:
    ret, img = flux.read()
    if not ret:
        print("Impossible d'obtenir une nouvelle image. Fin ...")
        break
    tps_attente = tps_img_sui - time.time_ns()
    if tps_attente > 0:
        time.sleep(tps_attente * 1e-9)
    cv2.imshow('Flux', img)
    tps_img_sui += 1 / fps * 1e9
    if cv2.pollKey() == ord('q'):
        break
flux.release()
cv2.destroyAllWindows()
