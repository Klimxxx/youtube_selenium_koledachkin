import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = ('xpath', '//select[@id="dropdown"]')

driver.get('https://the-internet.herokuapp.com/dropdown')

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

DROPDOWN.select_by_visible_text('Option 1')
time.sleep(3)

DROPDOWN.select_by_value('2')
time.sleep(3)

DROPDOWN.select_by_index(1)
time.sleep(3)

all_options = DROPDOWN.toptions

#perebor po texty
for option in all_options:
    if 'Option 2' in option.text:
        print('Опция 2 присутствует')
    DROPDOWN.select_by_visible_text(option.text)

#perebor po indexy
for option in all_options:
    DROPDOWN.select_by_index(all_options.index(option))

#perebor po value
for option in all_options:
    DROPDOWN.select_by_value(option.getattibute('value'))