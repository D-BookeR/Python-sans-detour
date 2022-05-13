try :
    x = int(input("Entrer un nombre : "))
except:
    print("ce n'est pas un nombre! valeur mise à un par défaut")
    x = 1
print("Le carré de ", x, " est ", x * x)
