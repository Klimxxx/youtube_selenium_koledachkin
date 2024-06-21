import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)


driver.get('https://demoqa.com/alerts')

#prinyatie alerta
BUTTON_1 = ('xpath', '//button[@id="alertButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.accept()

#otklonenie alerta
BUTTON_3 = ('xpath', '//button[@id="confirmButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
#print(alert.text)
alert.dismiss()

#alert s tekstom
BUTTON_4 = ('xpath', '//button[@id="confirmButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.send_keys('Hello world')
alert.accept()