import PySimpleGUI as sg


disposition = [[sg.Button('Ok', key='btn_1'),
                sg.Button('Quitter', key='btn_2')]]
fen_application = sg.Window('PYSimpleGUIWeb', disposition, resizable=True)
while True:
    event, values = fen_application.read()
    if event == sg.WIN_CLOSED:
        print("Case de fermeture")
        break
    if event in ('btn_1'):
        print("bouton ", event)
    elif event in ('btn_2'):
        print("bouton ", event)
        break
fen_application.close()
