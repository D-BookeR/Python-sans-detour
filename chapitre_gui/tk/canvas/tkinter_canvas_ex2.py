import tkinter

def tracer_canvas(le_graphique):
    le_graphique.create_oval(10,10,100,400)
    le_graphique.create_rectangle(220,230,410,420,
                                  fill='red',
                                  activefill='blue')
    for x in range(0,510,100):
        le_graphique.create_line(x, 0, x, 500)
    for y in range(0,510,100):
        le_graphique.create_line(0, y, 500, y, dash=(11, 5))
    mon_image = tkinter.PhotoImage(file='/tmp/python-logo-master-v3-TM.png')
    le_graphique.create_image(0, 0, image=mon_image, anchor=tkinter.NW)
    return mon_image

if __name__ == '__main__':
    fen_principale = tkinter.Tk(className="Usage canvas")
    graphique = tkinter.Canvas(fen_principale,height=500,width=500)
    mon_image = tracer_canvas(graphique)
    graphique.pack(side=tkinter.LEFT, fill = tkinter.BOTH)
    tkinter.mainloop()
