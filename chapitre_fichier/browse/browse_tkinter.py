import tkinter
import tkinter.filedialog

racine_tk = tkinter.Tk()
racine_tk.withdraw()
nom_classeur = tkinter.filedialog.askopenfilename(
        title='Choisir un fichier',
        filetypes=[('Classeur', '.xlsx')])
if len(nom_classeur) != 0:
    print("Chemin complet du fichier : ", nom_classeur)
else:
    print("L'utilisateur a cliqué dans annuler")
