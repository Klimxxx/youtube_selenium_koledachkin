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
#1
driver.get('https://the-internet.herokuapp.com/drag_and_drop')

COLUMN_A = ('xpath', '//div[@id="column-a"]')
COLUMN_B = ('xpath', '//div[@id="column-b"]')

A = driver.find_element(*COLUMN_A)
B = driver.find_element(*COLUMN_B)

time.sleep(3)
action.drag_and_drop(A, B).perform()
time.sleep(3)

#2
driver.get('https://tympanus.net/Development/DragDropInteractions/sidebar')

GRID_ITEM = ('xpath', '(//div[@class="grid__item"])[3]')
SIDEBAR_ITEM = ('xpath', '(//div[@class="drop-area__item"])[3]')

action.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()


