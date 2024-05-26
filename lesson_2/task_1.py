import time

from selenium import webdriver

driver = webdriver.Chrome()
PAGE_URL = driver.current_url
PAGE_TITLE = driver.title
driver.get("https://vk.com")
print(driver.title)
driver.get("https://google.com")
print(driver.title)
driver.back()
print(PAGE_URL)
assert PAGE_URL == "https://vk.com/", "Адрес неверный"
driver.refresh()
print(PAGE_URL)
driver.forward()
assert PAGE_URL == "https://google.com/", "Адрес не изменился"