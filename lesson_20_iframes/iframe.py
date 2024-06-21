import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options
options.add_argument('==window_size=1920, 1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

FORM_NAME_FIELD_LOCATOR = ('xpath', '//input[@id="RESULT_Text_Field-0"]')
COPY_TEXT_LOCATOR = ('xpath', '//button[text()="Copy Text"]')
IFRAME_LOCATOR = ('xpath', '//iframe')

driver.get('https://testautomationpractice.blogspot.com')
#1
driver.switch_to.frame('frame-one796456169')
#2
iframe = driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(iframe)
time.sleep(3)
driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys('Klim')
time.sleep(3)
driver.switch_to.default_content()
driver.find_element(*COPY_TEXT_LOCATOR).click()

#primer iframe v iframe
driver.get('https://demoqa.com/nestedframes')
driver.switch_to.frame('frame1')
print(driver.find_element('xpath', '//body').text)
# perekluchaemsya vnutri aifreima
driver.switch_to.frame(0)
print(driver.find_element('xpath', '//body').text)
# mozhno perecluchitsya k roditelskomy freimy
driver.switch_to.parent_frame()
print(driver.find_element('xpath', '//body').text)
