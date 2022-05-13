import tkinter
import tkinter.ttk

fen_principale = tkinter.Tk(className="Usage de pack")
fen_principale.geometry("350x150")
bouton = tkinter.ttk.Button(fen_principale, text="btn1")
bouton.pack(anchor=tkinter.S, expand=False, side=tkinter.RIGHT, fill=None, padx=0)

bouton = tkinter.ttk.Button(fen_principale, text="btn2")
bouton.pack(anchor=tkinter.NE, expand=True, side=tkinter.LEFT, fill=tkinter.X, padx=20)

bouton = tkinter.ttk.Button(fen_principale, text="btn3")
bouton.pack(anchor=tkinter.W, expand=True, side=tkinter.BOTTOM, fill=tkinter.Y, padx=10)
fen_principale.mainloop()