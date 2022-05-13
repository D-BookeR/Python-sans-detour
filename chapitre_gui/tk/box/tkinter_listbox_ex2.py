import tkinter
import tkinter.ttk


def gestion_boite_list(event):
    print(event.widget.curselection())
    mon_texte.set('Texte sélectionné :\n' +
                  event.widget.get(event.widget.curselection()))


fen_principale = tkinter.Tk(className="Usage Listbox")
choix_list_selec = tkinter.StringVar(value=('Choix 1',
                                            'Choix 2',
                                            'Choix 3',
                                            'Choix 4'
                                            )
                                     )
ma_boite_liste = tkinter.Listbox(fen_principale, listvariable=choix_list_selec)
ma_boite_liste.bind('<<ListboxSelect>>', gestion_boite_list)
ma_boite_liste.grid(column=0, row=0)
ma_boite_liste.selection_set(0)
mon_texte = tkinter.StringVar()
mon_texte.set('Texte sélectionné :\n' +
              ma_boite_liste.get(ma_boite_liste.curselection()))
ma_zone_texte = tkinter.ttk.Label(fen_principale, textvariable=mon_texte)
ma_zone_texte.grid(column=0, row=1)
fen_principale.mainloop()
