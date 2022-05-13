num_erreur = int(input("numéro de l'erreur "))

match num_erreur:
    case 401:
        print("Utilisateur non authentifié")
    case 403:
        print("Accès refusé")
    case 404:
        print("ressource non trouvée")
    case _:
        print("Erreur non répertiorée")
