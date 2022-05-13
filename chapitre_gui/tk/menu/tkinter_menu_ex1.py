import tkinter


def menu_nouveau():
    print("Menu nouveau")


def menu_ouvrir():
    print("Menu ouvrir")


def menu_sauver():
    print("Menu sauver")


fen_application = tkinter.Tk(className="Mon application")
barre_menu = tkinter.Menu(fen_application)
menu_fichier = tkinter.Menu(barre_menu, tearoff=0)
menu_fichier.add_command(label="Nouveau", command=menu_nouveau)
menu_fichier.add_command(label="Ouvrir", command=menu_ouvrir)
menu_fichier.add_command(label="Sauver", command=menu_sauver)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=fen_application.quit)
barre_menu.add_cascade(label="Fichier", menu=menu_fichier)

menu_apropos = tkinter.Menu(barre_menu, tearoff=0)
fen_application.configure(menu=barre_menu)
fen_application["menu"] = barre_menu
fen_application.mainloop()
fen_application.destroy()
