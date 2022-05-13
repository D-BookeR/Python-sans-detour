import tkinter
import tkinter.ttk


fen_principale = tkinter.Tk(className="Usage de pack")
fen_principale.geometry("250x100")
bouton = tkinter.Button(fen_principale, text="btn1")
bouton.pack(anchor=tkinter.S, expand=False, side=tkinter.RIGHT, fill=None, padx=10, pady=40)

bouton = tkinter.Button(fen_principale, text="btn2")
bouton.pack(anchor=tkinter.S, expand=False, side=tkinter.RIGHT, fill=None, padx=10, pady=40)

bouton = tkinter.Button(fen_principale, text="btn3")
bouton.pack(anchor=tkinter.S, expand=False, side=tkinter.RIGHT, fill=None, padx=10, pady=40)
fen_principale.mainloop()