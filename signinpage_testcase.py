from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

driver.find_element(By.ID,'nav-link-accountList-nav-line-1').click()

driver.quit()