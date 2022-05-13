commande = "aller vers le sud et rte z"
liste_mots = commande.split()
match liste_mots:
    case ["aller", "vers", "le", "nord" ]:
        print("Votre direction est le nord")
        print("Vous suivez un meridien")
    case ["aller", "vers", "le", "sud" ,*reste]:
        print("Votre direction est le sud")
        print("Vous suivez un meridien")
    case ["aller", "vers", "l'est" ]:
        print("Votre direction est l'est")
        print("Vous suivez un parallèle")
    case ["aller", "vers", "l'ouest" ]:
        print("Votre direction est l'ouest")
        print("Vous suivez un parallèle")
    case _:
        print("on est perdu")