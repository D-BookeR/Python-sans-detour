import tkinter


def gestion_ma_scale(event):
    print("valeur ", event)


fen_principale = tkinter.Tk(className="Usage Scale")
valeur_scale = tkinter.DoubleVar()
ma_scale = tkinter.Scale(fen_principale,
                         from_=-2.0,
                         to=2.0,
                         variable=valeur_scale,
                         resolution=0.1,
                         tickinterval=1,
                         label="Echelle",
                         command=gestion_ma_scale,
                         length=200,
                         orient=tkinter.HORIZONTAL)
ma_scale.set(0.7)
ma_scale.grid(column=0, row=0)
fen_principale.mainloop()
