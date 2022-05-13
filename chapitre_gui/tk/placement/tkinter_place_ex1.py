import tkinter
import tkinter.ttk

fen_principale = tkinter.Tk(className="Usage de place")
fen_principale.geometry("350x150")
bouton = tkinter.ttk.Button(fen_principale, text="btn1")
bouton.place(x=270, y=125, width=70, height=25)

bouton = tkinter.ttk.Button(fen_principale, text="btn2")
bouton.place(x=20, y=0, width=130, height=25)

bouton = tkinter.ttk.Button(fen_principale, text="btn3")
bouton.place(x=190, y=0, width=70, height=150)
fen_principale.mainloop()