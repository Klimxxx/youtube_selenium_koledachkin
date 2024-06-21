import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.yandex.ru')
time.sleep(10)
driver.get('https://www.google.com')

#metod vozvrazhaet nazad
driver.back()
time.sleep(3)

#metod vpered
driver.forward()
time.sleep(3)

#metod obnovleniya
driver.refresh()
time.sleep(3)




