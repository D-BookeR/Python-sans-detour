#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Exemple de recopie d'une page Web
sur le disque local
"""
import sys
import os
import urllib.request
import bs4


def lecture_page(url):
    """
    Lecture d'une page Web
    le paramètre url donne la valeur de l'URL à lire
    Si la page ne peut être lue, la valuer None est reournée
    Paramètre
    ----------
    url : type str

    valeur de retour
    -----------------
        page html de type bytes
    """
    try:
        with urllib.request.urlopen(url) as reponse:
            page = reponse.read()
    except urllib.request.HTTPError:
        page = None
        print(sys.exc_info())
    return page


def extraire_lien(liste_balises, attribut):
    """
    extraire les attributs et les mettre dans la liste
    liste_balises est le résultat de bs4.find_all
     Paramètre
    ----------
        liste_balises : type bs4.element.ResultSet (résultat de bs4.find_all)
        attribut : str

    valeur de retour
    -----------------
        liste des attributs extraits
    """
    balises_retenues = []
    for balise in liste_balises:
        lien_image = balise[attribut]
        balises_retenues.append(lien_image)
    return balises_retenues


def selection_lien_local(liens_selec):
    """
    sélection des liens interne au site Web
    Ils ne contiennent oas hhtp:// et https://
    Les liens contenant des ancres ou des requetes get
    sont modifiés

    Paramètre
    ----------
        liens_selec : list de str

    valeur de retour
    -----------------
        liste des liens pointant sur des ressources du site
    """
    liens_retenus = []
    for lien in liens_selec:
        if "//" in lien:
            pass
        else:
            nom = lien
            if '#' in lien:
                nom = nom[:nom.find("#")]
            if '?' in lien:
                nom = nom[:nom.find("?")]
            if nom:
                liens_retenus.append(nom)
    return liens_retenus


def copier_rsc(liste_lien, rep_local, proto_chemin):
    """
    Recopie des ressources pointées par des liens
    Les données seront recopiées rep_local
    en respectant l'arborescence relatif la page contenu
    chemin_page.
    proto_chemin est un tuple de 2 valeurs,
    le protocole et le chemin de la page

    Paramètre
    ----------
        liste_lien : list de str
        rep_local : type str
        proto_chemin

    valeur de retour
    -----------------
        aucune
    """
    for lien in liste_lien:
        pos_droite = lien.rfind("/")
        if lien[0] == '/':
            lien = lien[1:]
            pos_gauche = proto_chemin[1].find("/")
            repertoire_local = rep_local + proto_chemin[1][:pos_gauche]\
                + lien[:pos_droite]
        else:
            repertoire_local = rep_local + proto_chemin[1] + lien[:pos_droite]
        os.makedirs(repertoire_local, exist_ok=True)
        url_rsc = proto_chemin[0] + "://" + proto_chemin[1] + lien
        print("copie de = ", url_rsc)
        rsc_web = lecture_page(url_rsc)
        try:
            with open(rep_local + proto_chemin[1] + lien, "wb") as fichier:
                fichier.write(rsc_web)
        except (OSError, TypeError):
            print(sys.exc_info())
            print("Impossible d'écrire le fichier ",
                  rep_local + proto_chemin[1] + lien)


def extraire_rsc(balises, type_rsc, rep_local, proto_chemin):
    balises_ext = balises.find_all(type_rsc[0], **type_rsc[1])
    liens_elt = extraire_lien(balises_ext, list(type_rsc[1].keys())[0])
    print("elt_a_charger = ", liens_elt)
    liens_a_charger = selection_lien_local(liens_elt)
    print("elt_a_charger = ", liens_a_charger)
    copier_rsc(liens_a_charger, rep_local, proto_chemin)


if __name__ == '__main__':
    REP_LOCAL = "/tmp/"
#    URL_PAGE = "https://matplotlib.org/stable/tutorials/introductory/images.html"
    URL_PAGE = "https://matplotlib.org/stable/tutorials/index.html"
    protocole_adresse = URL_PAGE.split("://")
    if len(protocole_adresse) != 2:
        print("L'adresse ", URL_PAGE, " est mal construite.")
        sys.exit()
    adresse = protocole_adresse[1]
    chemin_url = os.path.dirname(adresse) + '/'
    nom_page = os.path.basename(adresse)
    print("En cours de traitement")
    print("nom de la page : ", nom_page)
    print("création de l'arborescence : ", REP_LOCAL + chemin_url)
    if os.path.splitdrive(os.getcwd())[0] != '':
        print("Le volume par défaut est ", os.path.splitdrive(os.getcwd())[0])
    try:
        os.makedirs(REP_LOCAL + chemin_url)
    except FileExistsError:
        print("arborescence déjà créée")
    page_web = lecture_page(URL_PAGE)
    if page_web is None:
        print("Désolé avec une page Web vide")
        print("Le programme s'arrête")
        sys.exit()
    try:
        with open(REP_LOCAL + chemin_url + nom_page, "wb") as f:
            f.write(page_web)
    except OSError:
        print(sys.exc_info())
        print("Erreur lors d'écriture de ", REP_LOCAL + chemin_url + nom_page)

    balises_page = bs4.BeautifulSoup(page_web, 'html.parser')
    type_balise = [("img", {"src": True}),
                   ("a", {"href": True}),
                   ("script", {"src": True}),
                   ("link", {"href": True})
                   ]
    for balise_act in type_balise:
        extraire_rsc(balises_page,
                     balise_act,
                     REP_LOCAL,
                     (protocole_adresse[0], chemin_url))
