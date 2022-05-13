try:
    x = int(input("Entrer un nombre : "))
    inverse_x = 1 / x
    print("L'inverse de ", x, " est ", 1 / x)
except ZeroDivisionError:
    print("0 n'a pas d'inverse :")
    print("il n'y a pas de nombre multiplié par 0 qui donne 1")
except ValueError:
    print("ce n'est pas un nombre! valeur mise à un par défaut")
    x = 1
    print("L'inverse de ", x, " est ", 1)
print("Le programme est terminé avec une gestion des erreurs")
