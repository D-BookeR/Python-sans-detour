import tkinter
import tkinter.messagebox


def menu_nouveau():
    tkinter.messagebox.showinfo(title="menu fichier",
                                message="Article Nouveau")


def menu_ouvrir():
    tkinter.messagebox.showinfo(title="menu fichier",
                                message="Article Ouvrir")


def menu_sauver():
    tkinter.messagebox.showinfo(title="menu fichier",
                                message="Article Sauver")


def control_o(event):
    print(event.x, event.y)
    menu_ouvrir()


def menu_aide():
    tkinter.messagebox.showinfo(title="menu aide",
                                message="Article aide")


def sous_menu_1():
    print("Sous Menu menu 1")


def sous_menu_2():
    print("Sous Menu menu 2")


def sous_menu_3():
    print("Sous Menu menu 3")


fen_application = tkinter.Tk(className="Mon application")
barre_menu = tkinter.Menu(fen_application)
menu_fichier = tkinter.Menu(barre_menu, tearoff=0)
menu_fichier.add_command(label="Nouveau", command=menu_nouveau)
menu_fichier.add_command(label="Ouvrir", command=menu_ouvrir)
cocher_sauver = tkinter.IntVar()
menu_fichier.add_checkbutton(label="Sauver",
                             command=menu_sauver,
                             variable=cocher_sauver)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=fen_application.quit)
menu_fichier.entryconfigure('Ouvrir', accelerator='Ctrl+o')
fen_application.bind("<Control-o>", control_o)
barre_menu.add_cascade(label="Fichier", menu=menu_fichier)
menu_apropos = tkinter.Menu(barre_menu, tearoff=0)
menu_apropos.add_command(label="Aide", command=menu_aide)
sous_menu = tkinter.Menu(barre_menu, tearoff=0)
sous_menu.add_command(label="Sous-menu 1", command=sous_menu_1)
sous_menu.add_command(label="Sous-menu 2", command=sous_menu_2)
sous_menu.add_command(label="Sous-menu 3", command=sous_menu_3)
menu_apropos.add_cascade(label="Sous-menu", menu=sous_menu)

barre_menu.add_cascade(label="A propos", menu=menu_apropos)
fen_application["menu"] = barre_menu
fen_application["bg"] = 'grey'
fen_application["width"] = 900
fen_application["height"] = 100
fen_application.mainloop()
fen_application.destroy()
