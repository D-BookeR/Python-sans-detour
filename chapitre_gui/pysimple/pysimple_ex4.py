import PySimpleGUIWeb as sg

def bouton_ok():
    sg.popup_ok("Vous avez cliqué dans le bouton OK")

    
if __name__ == '__main__':
    disposition = [[sg.Button('Ok', key=bouton_ok)],
                   [sg.Button('Quitter', key='btn_2')]]
    fen_application = sg.Window('PYSimpleGUI', disposition, resizable=True)
    while True:
        event, values = fen_application.read()
        if event in (sg.WIN_CLOSED, 'btn_2'):
            print("Case de fermeture ou bouton quitter")
            break
        if callable(event):
            event()
    fen_application.close()
