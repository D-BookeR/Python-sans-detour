import tkinter


def event_clavier(event, l_param):
    if event.char == 'r':
        l_param[0] = 'red'
    elif event.char == 'v':
        l_param[0] = 'green'
    elif event.char == 'b':
        l_param[0] = 'blue'

def clic_gauche_souris(event, l_param):
    event.widget.focus_set()
    event.widget.create_rectangle(event.x, event.y,
                                  event.x + 10, event.y + 10,
                                  fill=l_param[0])

def clic_droite_souris(event, l_param):
    event.widget.focus_set()
    event.widget.create_oval(event.x, event.y,
                             event.x + 10, event.y + 10,
                             fill=l_param[0])


if __name__ == '__main__':
    fen_principale = tkinter.Tk(className="Usage Canvas et bind")
    graphique = tkinter.Canvas(fen_principale)
    l_parametre = ['red']
    graphique.bind("<Key>",
                   lambda evt: event_clavier(evt, l_parametre))
    graphique.bind("<Button-1>",
                   lambda evt: clic_gauche_souris(evt, l_parametre))
    graphique.bind("<Button-3>",
                   lambda evt: clic_droite_souris(evt, l_parametre))
    graphique.pack()
    tkinter.mainloop()
