#!/usr/bin/env python
import PySimpleGUIWeb as sg


valeur_table = []
for lig in range(10, 120, 2):
    valeur_table.append([str(lig), str(lig * lig), str(lig // 3)])
titre_colonne = ['Valeurs', 'Carré de la valeur', 'Tiers de la valeur']
disposition = [[sg.Button('Quitter', key='btn_1')],
               [sg.Table(values=valeur_table,
                         key='_MonTableau_',
                         display_row_numbers=True,
                         auto_size_columns=True,
                         headings=titre_colonne,
                         background_color='white',
                         text_color='black',
                         enable_events=True,
                         num_rows=20,
                         )
                ]
               ]
window = sg.Window('Table', disposition)
while True:
    event, valeurs_evt = window.read()
    if event in (sg.WIN_CLOSED, 'btn_1'):
        break
    if event == '_MonTableau_':
        print(valeurs_evt)
window.close()
