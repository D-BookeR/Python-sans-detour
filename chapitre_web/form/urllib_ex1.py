import urllib.parse
import urllib.request


requete_post = dict(
    var_nom='Hugo',
    var_prenom='Victor')
requete = urllib.parse.urlencode(requete_post)
requete_encode = requete.encode('utf-8')
reponse_post = urllib.request.Request(
      "https://www.traimaocv.fr/action_page.php",
      data=requete_encode, method='POST')
with urllib.request.urlopen(reponse_post) as lien_page:
    page = lien_page.read()
print(page.decode('utf-8'))
