import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org')
url = driver.current_url
print(f'URL stranici {url}')
current_title = driver.title
print(f"Tekushii zagolovok {current_title}")

assert url == 'https://www.wikipedia.org', 'Oshibka v URL, otkrita ne ta stranica'
assert current_title == 'wikipedia', 'Nekorrektnii zagolovok'

print(driver.page_source)
time.sleep(3)


