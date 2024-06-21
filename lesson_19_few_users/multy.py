from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options
options.add_argument('==window_size=1920, 1080')
service = Service(executable_path=ChromeDriverManager().install())
driver_1 = webdriver.Chrome(service=service, options=options)

LOGIN_FIELD = ('xpath', '//input[@type="email"')
PASSWORD_FIELD = ('xpath', '//input[@type="password"]')
SUBMIT_BUTTON = ('xpath', '//button[@type="submit"]')

driver_1.get('hhtps://hyperskill.org/login')
driver_1.find_element(*LOGIN_FIELD).send_keys('alekseik@ya.ru')
driver_1.find_element(*PASSWORD_FIELD).send_keys('qwerty132!')
driver_1.find_element(*SUBMIT_BUTTON).click()

driver_2 = webdriver.Chrome(service=service, options=options)
driver_2.get('hhtps://hyperskill.org/login')
