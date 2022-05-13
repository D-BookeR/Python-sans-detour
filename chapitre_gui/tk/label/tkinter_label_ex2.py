import tkinter


fen_principale = tkinter.Tk(className="Usage label")
mon_texte = tkinter.StringVar()
mon_texte.set('Texte sélectionné :' + 'F')
mon_image = tkinter.PhotoImage(file='/tmp/ma_carte.png')
ma_zone_texte = tkinter.Label(fen_principale, image=mon_image)
ma_zone_texte.grid(column=0,row=1)
fen_principale.mainloop()
