import base64
import urllib
import selenium.webdriver
import selenium.webdriver.support.wait
import selenium.webdriver.support.expected_conditions

navigateur = selenium.webdriver.Firefox()
freq_phase = [(1.23, 4.56), (2, 4.56)]
for idx, f_p in enumerate(freq_phase):
    navigateur.get('https://exemple.traimaocv.fr/index/frequence')
    freq = navigateur.find_element(selenium.webdriver.common.by.By.NAME,
                                   "freq")
    freq.clear()
    freq.send_keys(str(f_p[0]))
    phase = navigateur.find_element(selenium.webdriver.common.by.By.NAME,
                                    "phase")
    phase.clear()
    phase.send_keys(str(f_p[1]))
    phase.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
    attente = selenium.webdriver.support.wait.\
        WebDriverWait(navigateur,
                      20)
    condition = selenium.webdriver.support.expected_conditions.\
        presence_of_element_located((selenium.webdriver.common.by.By.XPATH,
                                     "//html/body/img"))
    attente.until(condition)
    balise_img = navigateur.find_element(selenium.webdriver.common.by.By.XPATH,
                                         "//html/body/img")
    src = balise_img.get_attribute('src')
    data_png = base64.b64decode(urllib.parse.unquote(src[22:]))
    with open("/tmp/index_decode" + str(idx) + ".png", "wb") as f:
        buf = f.write(data_png)
navigateur.quit()
