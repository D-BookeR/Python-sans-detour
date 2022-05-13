import tkinter


def gestion_boite_list(event):
    print(ma_boite_liste.curselection())
    print(ma_boite_liste.get(ma_boite_liste.curselection()))


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
fen_principale.mainloop()
