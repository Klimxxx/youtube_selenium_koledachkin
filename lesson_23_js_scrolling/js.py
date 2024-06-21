import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from lesson_23_js_scrolling.scrolls import Scrolls

options = Options
options.add_argument('==window_size=1920, 1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

action = ActionChains(driver)
driver.get('https://seiyria.com/bootstrap-slider')

#driver.execute("alert('Hello')")

EX_2_LOCATOR = ('xpath', '//h3[text()="Example 2: "]')
EX_2 = driver.find_element(*EX_2_LOCATOR)


Scrolls.scroll_to_element(EX_2)