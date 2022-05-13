import time
import selenium.webdriver

navigateur = selenium.webdriver.Firefox()
navigateur.get('https://www.traimaocv.fr/form_php.html')
nom = navigateur.find_element(selenium.webdriver.common.by.By.NAME,
                              "var_nom")
nom.clear()
nom.send_keys("Hugo")
prenom = navigateur.find_element(selenium.webdriver.common.by.By.NAME,
                                 "var_prenom")
prenom.clear()
prenom.send_keys("Victor")
bouton = navigateur.find_element(selenium.webdriver.common.by.By.XPATH,
                                 "//input[@type='submit']")
bouton.click()
time.sleep(1)
page = navigateur.find_element(selenium.webdriver.common.by.By.XPATH,
                               "//body")
print(page.text)
navigateur.quit()
