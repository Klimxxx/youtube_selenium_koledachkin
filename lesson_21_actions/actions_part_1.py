import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options
options.add_argument('==window_size=1920, 1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

action = ActionChains(driver)

LEFT_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id=["leftClick"]')
DOUBLE_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id=["doubleClick"]')
RIGHT_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id=["rightClick"]')
HOVER_BUTTON_LOCATOR = ('xpath', '//button[@id=["colorChangeOnHover"]')


driver.get('https://testkru.com/Elements/Buttons')

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
action.click(left_button).perform()

double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
action.double_click(double_button).perform()

right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
action.context_click(right_button).perform()

#vot esli nyzhno vipolnit cepochky deistvii
action.click(left_button).double_click(double_button).context_click(right_button).perform()

#esli nyzhno vizvat pausy
action.click(left_button).pause(3).double_click(double_button).pause(3).context_click(right_button).perform()

hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)
action.move_to_element(hover_button).perform()

#drugoi primer
driver.get('https://demoqa.com/menu')

MENU_ITEM_2_LOCATOR = ('xpath', '//a[text()="Main Item 2"]')
SUB_LIST_LOCATOR = ('xpath', '//a[text()="SUB SUB LIST »"]')

menu_item_2 = driver.find_element(*MENU_ITEM_2_LOCATOR)
sub_list_menu = driver.find_element(*SUB_LIST_LOCATOR)

action.move_to_element(menu_item_2)\
    .pause(2)\
    .move_to_element(sub_list_menu)\
    .perform()

