
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

#1
# CHECKBOX_1 = ('xpath', '(//input[@type="checkbox"])[1]')
#
# driver.get('https://the-internet.herocuapp.com/checkboxes')
#
# driver.find_element(*CHECKBOX_1).click()
# #proverka chto checkbox vibran
# assert driver.find_element(*CHECKBOX_1).get_attribute('checked') is not None
# #libo mozhno 2 sposob - specialnii metod
# assert driver.find_element(*CHECKBOX_1).is_selected() is True
#
# #2
# CHECKBOX_HOME_STATUS = ('xpath', '//input[@id="tree-node-home"]')
# CHECKBOX_HOME_ACTION = ('xpath', '//span[@class="rct-checkbox"]')
#
# driver.get('https"//demoqa.com/checkbox')
# driver.find_element(*CHECKBOX_HOME_ACTION).click()
# assert driver.find_element(*CHECKBOX_HOME_STATUS).is_selected() is True

#3
ELEMENT_ONE = ('xpath', '//li[text()="Cras justo odio"]')
YES_RADIO_STATUS = ('xpath', '//input[@id="yesRadio"]')
YES_RADIO_ACTION = ('xpath', '//label[@for="yesRadio"]')
NO_RADIO_STATUS = ('xpath', '//input[@id="noRadio"]')
NO_RADIO_ACTION = ('xpath', '//label[@for="noRadio"]')

driver.get('https://demoqa.com/selectable')

#ckeckboxs
before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
print(before)
driver.find_element(*ELEMENT_ONE).click()
after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
print(after)
assert "active" in after
#if "active" in after:
#print("click ok")'

#radiobuttons
print(driver.find_element(*YES_RADIO_ACTION).is_selected())
driver.find_element(*YES_RADIO_ACTION).click()
print(driver.find_element(*YES_RADIO_ACTION).is_selected())

#status disabled radiobutton
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
