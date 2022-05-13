import tkinter
import tkinter.ttk


def gestion_bouton_ok():
    print("Bouton OK")
    print("Cliquer sur le bouton annuler pour fermer la fenêtre")


def changement_onglet(event):
    print('onglet ', event.widget.index(event.widget.select()), " : ",
          event.widget.tab(event.widget.select(), "text"))


if __name__ == '__main__':
    fen_principale = tkinter.Tk(className="Usage notebook")
    carnet = tkinter.ttk.Notebook(fen_principale, width=400)
    cadre_1 = tkinter.ttk.Frame(carnet)
    bouton_ok = tkinter.ttk.Button(cadre_1,
                                   text="OK!",
                                   command=gestion_bouton_ok)
    bouton_annuler = tkinter.ttk.Button(cadre_1,
                                        text="Annuler",
                                        command=fen_principale.destroy)

    bouton_ok.grid(column=0, row=0)
    bouton_annuler.grid(column=0, row=1)
    cadre_2 = tkinter.ttk.Frame(carnet)
    graphique = tkinter.Canvas(cadre_2)
    graphique.create_oval(10, 10, 100, 100)
    graphique.pack()
    carnet.add(cadre_1, text='Onglet avec boutons')
    carnet.add(cadre_2, text='Onglet avec canvas')
    carnet.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    carnet.bind("<<NotebookTabChanged>>", changement_onglet)
    fen_principale.mainloop()
