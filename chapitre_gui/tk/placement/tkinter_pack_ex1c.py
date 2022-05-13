import tkinter
import tkinter.ttk


fen_principale = tkinter.Tk(className="Usage de pack")
fen_principale.geometry("250x100")
bouton = tkinter.Button(fen_principale, text="btn1")
bouton.pack(anchor=tkinter.N, expand=True, side=tkinter.TOP, fill=tkinter.X, padx=10, pady=5)

bouton = tkinter.Button(fen_principale, text="btn2")
bouton.pack(anchor=tkinter.N, expand=True, side=tkinter.TOP, fill=tkinter.X, padx=10, pady=5)

bouton = tkinter.Button(fen_principale, text="btn3")
bouton.pack(anchor=tkinter.N, expand=True, side=tkinter.TOP, fill=tkinter.X, padx=10, pady=5)
fen_principale.mainloop()