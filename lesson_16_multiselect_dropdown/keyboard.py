import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1 obichnie selecti
# KEYBOARD_INPUT = ('xpath', '//input[@id="target"]')
# driver.get('https://www.the-internet.herokuapp.com/key_presses')
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.COMMAND + "A")

# 2 sovremennie selecti na divah
# v konsoli mozhno vvesti cod dlya ostanovki debugga cherez 5 sekund
# setTimeout(function() { debugger; }, 5000);
SELECT_LOCATOR = ('xpath', '//input[@id="reactselect-3-input"]')
SELECT_ONE = ('xpath', '//div[@id="selectOne"]')
PROF_OPTION = ('xpath', '//div[text()="Prof"]')
MULTISELECT_LOCATOR = ('xpath', '//input[@id="react-select-4-input"]')

driver.get('https://demoqa.com/select-menu')

driver.find_element(*SELECT_LOCATOR).send_keys('Ms.')
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)

#2
driver.find_element(*SELECT_ONE).click()
driver.find_element(*PROF_OPTION).click()

#3 multiselect

driver.find_element(*MULTISELECT_LOCATOR).send_keys('Green')
#mozhno TAB zamenit na ENTER
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)

#takze TAB dozavershatn slovo Black
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Bla')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)