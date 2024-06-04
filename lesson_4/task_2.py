import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
USERNAME_INPUT_LOCATOR = ('xpath', "//input[@id='username']")
PASSWORD_INPUT_LOCATOR = ('xpath', "//input[@id='password']")
SUBMIT_BUTTON_LOCATOR = ('xpath', "//button[@type='submit']")
LOGOUT_BUTTON_LOCATOR = ('xpath', "//a[@class='button secondary radius']")


username_input = driver.find_element(*USERNAME_INPUT_LOCATOR)
password_input = driver.find_element(*PASSWORD_INPUT_LOCATOR)
submit_button = driver.find_element(*SUBMIT_BUTTON_LOCATOR)

username_input.clear()
username_input.send_keys("tomsmith")

password_input.clear()
password_input.send_keys("SuperSecretPassword!")

submit_button.click()

logout_button = driver.find_element(*LOGOUT_BUTTON_LOCATOR)
assert logout_button.is_displayed()