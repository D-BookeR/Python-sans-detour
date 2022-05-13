import tkinter


fen_principale = tkinter.Tk(className="Usage label")
mon_texte = tkinter.StringVar()
mon_texte.set('Ceci est un Texte')
ma_zone_texte = tkinter.Label(fen_principale, textvariable=mon_texte)
ma_zone_texte.grid(column=0,row=0)
fen_principale.mainloop()
