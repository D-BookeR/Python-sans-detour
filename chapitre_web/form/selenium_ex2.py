import selenium.webdriver
import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.wait

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
prenom.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
condition = selenium.webdriver.\
    support.expected_conditions.title_is("Résultat requête")
selenium.webdriver.support.wait.WebDriverWait(navigateur,
                                              3).until(condition)
page = navigateur.find_element(selenium.webdriver.common.by.By.XPATH, "//body")
print(page.text)
navigateur.quit()
