import googlesearch
resultat = googlesearch.search("python gestionnaire de contexte",
                               num=10,
                               lang="fr",
                               stop=10)
for idx, site in enumerate(resultat):
    print("Résultat ", idx, " -> ", site)
