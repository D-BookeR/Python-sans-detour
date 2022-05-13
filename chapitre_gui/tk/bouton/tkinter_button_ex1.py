import tkinter


def gestion_bouton_ok():
    print("Bouton OK")
    print("Cliquer sur le bouton annuler pour fermer la fenêtre")


fen_application = tkinter.Tk(className="Mon application")
bouton_ok = tkinter.Button(fen_application,
                           text="OK!",
                           command=gestion_bouton_ok)
bouton_annuler = tkinter.Button(fen_application,
                                text="Annuler",
                                command=fen_application.quit)
bouton_ok.grid(column=0, row=0)
bouton_annuler.grid(column=0, row=1)
fen_application.mainloop()
