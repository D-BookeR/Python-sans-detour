import tkinter
import tkinter.ttk

fen_principale = tkinter.Tk(className="Usage de grid")
fen_principale.geometry("400x300")
cadre = tkinter.Frame(fen_principale, bg="red", borderwidth=50, relief=tkinter.RAISED)
for ind in range(5):
    bouton = tkinter.ttk.Button(cadre, text="btn1_" + str(ind))
    bouton.grid(row=ind//2, column=ind % 2)
cadre.grid(row=0, column=0, rowspan=3, columnspan=2)
cadre = tkinter.Frame(fen_principale, bg="blue", borderwidth=50, relief=tkinter.SUNKEN)
for ind in range(8):
    bouton = tkinter.ttk.Button(cadre, text="btn2_" + str(ind))
    bouton.grid(row=ind//4, column=ind % 4)
cadre.grid(row=1, column=2, rowspan=2, columnspan=4)
cadre = tkinter.Frame(fen_principale, bg="green", borderwidth=50, relief=tkinter.RIDGE)
for ind in range(6):
    bouton = tkinter.ttk.Button(cadre, text="btn3_" + str(ind))
    bouton.grid(row=ind//4, column=ind % 4)
cadre.grid(row=3, column=0, columnspan=4, rowspan=2)
fen_principale.mainloop()
