#ne rabotaet kod

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

PROXY_SERVER = '51.222.220.236:32769'

options = Options()
options.add_argument(f'--proxy-server={PROXY_SERVER}')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://whoer.net/ru')
time.sleep(5)

#driver.quit()
