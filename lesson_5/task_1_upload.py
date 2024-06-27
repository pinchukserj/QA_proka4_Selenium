import os.path
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")
file_input = driver.find_element('xpath', "//input[@id='uploadFile']")
file_input.send_keys(os.path.join(os.getcwd(), "sampleFile.jpeg"))
time.sleep(5)