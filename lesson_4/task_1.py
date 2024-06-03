import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')

full_name = driver.find_element('xpath', "//input[@id='userName']")
full_name.clear()
full_name.send_keys("IVAN IVANOV")
assert "IVAN IVANOV" in full_name.get_attribute("value")

email = driver.find_element('xpath', "//input[@id='userEmail']")
email.clear()
email.send_keys("test@test.com")
assert "test@test.com" in email.get_attribute("value")

current_address = driver.find_element('xpath', "//textarea[@id='currentAddress']")
current_address.clear()
current_address.send_keys("qwerty")
assert "qwerty" in current_address.get_attribute("value")

permanent_address = driver.find_element('xpath', "//textarea[@id='permanentAddress']")
permanent_address.clear()
permanent_address.send_keys('zxcvbn')
assert 'zxcvbn' in permanent_address.get_attribute("value")