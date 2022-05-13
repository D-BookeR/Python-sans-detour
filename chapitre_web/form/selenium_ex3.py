import selenium.webdriver
import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.wait

navigateur = selenium.webdriver.Firefox()
navigateur.get('https://www.traimaocv.fr/form_php_tab.html')
nom = navigateur.find_element(selenium.webdriver.common.by.By.NAME,
                              "var_nom")
nom.clear()
nom.send_keys("Hugo")
prenom = navigateur.find_element(selenium.webdriver.common.by.By.NAME,
                                 "var_prenom")
prenom.clear()
prenom.send_keys("Victor")
nb_onglet = len(navigateur.window_handles)
prenom.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
attente = selenium.webdriver.support.wait.\
              WebDriverWait(navigateur,
                            20)
condition = selenium.webdriver.support.expected_conditions.\
    number_of_windows_to_be(nb_onglet+1)
attente.until(condition)
navigateur.switch_to.window(navigateur.window_handles[-1])
condition = selenium.webdriver.support.expected_conditions.\
    title_is("Résultat requête")
page = attente.until(condition)
condition = selenium.webdriver.support.expected_conditions.\
    presence_of_element_located((selenium.webdriver.common.by.By.XPATH,
                                 "//body"))
page = attente.until(condition)
print(page.text)
navigateur.quit()
