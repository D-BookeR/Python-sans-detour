import tkinter
import tkinter.ttk


def gestion_ma_spinbox_plus(event):
    print("Plus haut ", event.widget.get())


def gestion_ma_spinbox_moins(event):
    print("Plus bas ", event.widget.get())


fen_principale = tkinter.Tk(className="Usage Spinbox")
ma_spinbox = tkinter.ttk.Spinbox(fen_principale,
                                 from_=1.0,
                                 to=10,
                                 increment=0.5)
ma_spinbox.set('0.5')
ma_spinbox.bind('<<Increment>>', gestion_ma_spinbox_plus)
ma_spinbox.bind('<<Decrement>>', gestion_ma_spinbox_moins)
ma_spinbox.grid(column=0, row=0)
fen_principale.mainloop()
