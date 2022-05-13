import selenium.webdriver

navigateur = selenium.webdriver.Firefox()
navigateur.get('https://www.traimaocv.fr/affiche_header.php')
navigateur.quit()