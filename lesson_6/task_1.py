from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)

CHANGE_TEXT_BUTTON_LOCATOR = ('xpath', "//button[@id='populate-text']")
DISPLAY_OTHER_BUTTON_LOCATOR = ('xpath', "//button[@id='display-other-button']")
ENABLE_BUTTON_LOCATOR = ('xpath', "//button[@id='enable-button']")
HIDDEN_BUTTON_LOCATOR = ('xpath', "//button[@id='hidden']")
DISABLE_BUTTON_LOCATOR = ('xpath', "//button[@id='disable']")
ALERT_BUTTON_LOCATOR = ('xpath', "//button[@id='alert']")
TEXT_LOCATOR = ('xpath', "//h2[@id='h2']")

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.find_element(*CHANGE_TEXT_BUTTON_LOCATOR).click()
wait.until(EC.text_to_be_present_in_element(TEXT_LOCATOR, "Selenium Webdriver"))

driver.find_element(*DISPLAY_OTHER_BUTTON_LOCATOR).click()
wait.until(EC.presence_of_element_located(HIDDEN_BUTTON_LOCATOR))

driver.find_element(*ENABLE_BUTTON_LOCATOR).click()
wait.until(EC.element_to_be_clickable(DISABLE_BUTTON_LOCATOR))

driver.find_element(*ALERT_BUTTON_LOCATOR).click()
wait.until(EC.alert_is_present())



