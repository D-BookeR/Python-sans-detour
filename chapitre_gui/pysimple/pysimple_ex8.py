import sys
import PySimpleGUIWeb as sg
import cv2


vid = cv2.VideoCapture(0, cv2.CAP_ANY)
if not vid.isOpened():
    print("Erreur lors de la lecture du flux")
    sys.exit()
couleur = True
val_zoom = 0.25
zone_image = sg.Image()
case_couleur = sg.Checkbox('Couleur',
                           key="__COULEUR__",
                           default=couleur,
                           enable_events=True)
choix_zoom = sg.Combo(values=('0.25', '0.5', '1', '2'),
                      default_value=str(val_zoom),
                      key="__ZOOM__",
                      enable_events=True)
disposition = [[zone_image],
               [case_couleur, choix_zoom],
               [sg.Button('Quitter')],
               ]
window = sg.Window('Webcam',
                   disposition,
                   web_port=1023,
                   web_start_browser=True)
while True:
    event, valeurs = window.read(timeout=100)
    status, img = vid.read()
    if event in (sg.WIN_CLOSED, 'Quitter'):
        break
    if callable(event):
        event()
    elif event in ('__ZOOM__'):
        val_zoom = float(valeurs["__ZOOM__"])
    elif event in ('__COULEUR__'):
        couleur = valeurs["__COULEUR__"]
    elif status:
        if not couleur:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (0, 0), fx=val_zoom, fy=val_zoom)
        st_encode, tampon = cv2.imencode(".png", img)
        zone_image.update(data=tampon.tobytes())
vid.release()
window.close()



