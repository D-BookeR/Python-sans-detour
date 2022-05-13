import tkinter

fen_principale = tkinter.Tk(className="Usage Scrollbar")
scrollbar = tkinter.Scrollbar(fen_principale)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
ma_liste = tkinter.Listbox(fen_principale, yscrollcommand=scrollbar.set)
for choix in range(100):
    ma_liste.insert(tkinter.END, "Ligne " + str(choix))
ma_liste.pack(expand=True,side=tkinter.LEFT, fill=tkinter.BOTH)
scrollbar.config(command=ma_liste.yview)
tkinter.mainloop()
