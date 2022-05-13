import tkinter


fen_principale = tkinter.Tk(className="Usage Canvas")
graphique = tkinter.Canvas(fen_principale)
graphique.create_oval(10,10,100,100)
graphique.pack()
tkinter.mainloop()
