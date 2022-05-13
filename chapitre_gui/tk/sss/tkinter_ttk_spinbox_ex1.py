import tkinter
import tkinter.font


def gestion_ma_spinbox_plus(event):
    print("Plus haut ", event.widget.get())


def gestion_ma_spinbox_moins(event):
    print("Plus bas ", event.widget.get())


fen_principale = tkinter.Tk(className="Usage Spinbox")
choix_spinbox_selec = tkinter.StringVar()
valeurs_possibles = ['Choix 1',
                     'Choix 2',
                     'Choix 3',
                     'Choix 4']
choix_spinbox_selec.set(valeurs_possibles[1])
ma_spinbox = tkinter.Spinbox(fen_principale,
                                 textvariable=choix_spinbox_selec,
                                 value=valeurs_possibles,
                                 width=7,
                                 state='readonly',
                                 font=tkinter.font.Font(size=18, slant='italic'))
ma_spinbox.bind('<<Increment>>', gestion_ma_spinbox_plus)
ma_spinbox.bind('<<Decrement>>', gestion_ma_spinbox_moins)
ma_spinbox.grid(column=0, row=0)
fen_principale.mainloop()
