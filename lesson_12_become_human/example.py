import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
#options.add_argument('--headless')
#options.add_argument('--window-size=1920,1080')
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--user-agent=Chrome/42.0.2311.135')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get(os.environ['STAGE_URL'])
# driver.save_screenshot('screen.png')
#wait.until(EC.title_is('What Is My IP Address - See Your Public Address - IPv4 & IPv6'))

LOGIN_BUTTON = ('xpath', '//div[@data-testid="open-login-modal"]')
PHONE_INPUT = ('xpath', '//input[@id="phone"]')



driver.find_element(*LOGIN_BUTTON).click()
wait.until(EC.presence_of_element_located(PHONE_INPUT)).send_keys(os.environ['PHONE_NUMBER'])

time.sleep(100)
