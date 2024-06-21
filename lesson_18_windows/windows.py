import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--window-size=1920, 1080')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

FOR_BUSINESS = ('xpath', '(//a[text()=" For Business"]')
START_FREE_BUTTON_LOCATOR = ('xpath', '(//a[text()="Start for Free"])')

#1
driver.get('https://hyperskill.org/tracks')
time.sleep(3)

# print(driver.current_window_handle)
# print(driver.window_handles)
driver.find_element(*FOR_BUSINESS).click()
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
#driver.switch_to.window(driver.window_handles[1])

driver.find_element(*START_FREE_BUTTON_LOCATOR)
time.sleep(3)

#2
driver.get('https://hyperskill.org/tracks')
time.sleep(5)

windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.get('https://ya.ru')
time.sleep(3)

#3
driver.switch_to.new_window('tab')
#vmesto tab mozhno window
