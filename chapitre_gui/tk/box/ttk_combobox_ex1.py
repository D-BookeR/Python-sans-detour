import tkinter
import tkinter.ttk


def gestion_ma_combobox(event):
    print(event.widget.get())
    mon_texte.set('Texte sélectionné :\n' + event.widget.get())


fen_principale = tkinter.Tk(className="Usage Combobox")
choix_comobo_selec = tkinter.StringVar()
valeurs_possibles = ['Choix 1',
                     'Choix 2',
                     'Choix 3',
                     'Choix 4']
choix_comobo_selec.set(valeurs_possibles[1])
ma_boite_combo = tkinter.ttk.Combobox(fen_principale,
                                      textvariable=choix_comobo_selec,
                                      value=valeurs_possibles)
ma_boite_combo.bind('<<ComboboxSelected>>', gestion_ma_combobox)
ma_boite_combo.grid(column=0, row=1)
mon_texte = tkinter.StringVar()
mon_texte.set('Texte sélectionné :' + ma_boite_combo.get())
ma_zone_texte = tkinter.ttk.Label(fen_principale, textvariable=mon_texte)
ma_zone_texte.grid(column=0, row=0)
fen_principale.mainloop()
