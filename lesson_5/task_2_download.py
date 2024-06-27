import os
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1280,800")
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "downloads"),
    "safebrowsing.enabled" : True,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(5)
links = driver.find_elements("xpath", "//div[@id='content']//a")
for link in links:
    link.click()