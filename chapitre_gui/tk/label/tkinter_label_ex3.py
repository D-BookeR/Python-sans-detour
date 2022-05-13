import tkinter


fen_principale = tkinter.Tk(className="Usage label")
mon_texte = tkinter.StringVar()
mon_texte.set('Texte du label')
mon_image = tkinter.PhotoImage(file='/tmp/python-logo-master-v3-TM.png')
ma_zone_texte = tkinter.Label(fen_principale,
                              image=mon_image,
                              textvariable=mon_texte,
                              compound=tkinter.BOTTOM)
ma_zone_texte.grid(column=0,row=1)
fen_principale.mainloop()
