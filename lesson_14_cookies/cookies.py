import os
import time
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/en/us/login')
#pechataem 1 kyky v konsol
print(driver.get_cookie('country_code'))
#pechataem vse kyki v konsol
print(driver.get_cookies())
#dobavlyaem 1 kyky
driver.add_cookie({
    'name' : 'Example',
    'value' : 'Kykyshka'
})
#proveryaem chto kyka dobavilas
print(driver.get_cookie('Example'))

#zamena 1 kyki
before = driver.get_cookie('split')
print(before)
driver.delete_cookie('split')
driver.add_cookie({
    'name' : 'split',
    'value' : 'qwerty'
})
after = driver.get_cookie('split')
print(after)

#zamena vseh kyki
before = driver.get_cookies()
print(before)
driver.delete_all_cookies()
driver.add_cookie({
    'name' : 'split',
    'value' : 'qwerty'
})
after = driver.get_cookies()
print(after)

#чтобы сохранить все куки (например когда не знаешь какая одна нужна для регистрации)
#сначала нужно авторизоваться
pickle.dump(driver.get_cookies(), open(os.getcwd()+'/cookies/cookies.pkl', 'wb'))

driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd() +'/cookies/cookies.pkl', 'rb'))

for cookie in cookies:
    driver.add_cookie(cookie)
#чтобы куки применились
driver.refresh()