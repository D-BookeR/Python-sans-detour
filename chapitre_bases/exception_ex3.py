while True:
    x = input("Entrer un texte : ")
    if x == "au revoir":
        raise ValueError('Le texte au revoir déclenche une exception')
    print("Jusqu'ici tout va bien!")
