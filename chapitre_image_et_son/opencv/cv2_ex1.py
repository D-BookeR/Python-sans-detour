import sys
import cv2


flux = cv2.VideoCapture(0, cv2.CAP_ANY)
if not flux.isOpened():
    print("Le flux ne peut être ouvert")
    sys.exit()
while True:
    ret, img = flux.read()
    if not ret:
        print("erreur ou fin de la lecture du flux.")
        break
    cv2.imshow('Webcam', img)
    if cv2.pollKey() == ord('q'):
        break
flux.release()
cv2.destroyAllWindows()
