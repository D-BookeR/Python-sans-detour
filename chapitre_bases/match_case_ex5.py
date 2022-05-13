commande = "aller vers le nord"
liste_mots = commande.split()
meridien = {"nord", "sud"}
match liste_mots:
    case ["aller", "vers", "le", direction] if direction in meridien:
        print("Votre direction est le",direction)
        print("Vous suivez un meridien")
    case ["aller", "vers", ("l'est" | "l'ouest") as direction]:
        print("Votre direction est",direction)
        print("Vous suivez donc un parallèle")
    case _:
        print("on est perdu")