from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

driver.find_element(By.ID,'nav-orders').click()

expected_text= 'Sign-In'
actual_text= driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text
assert expected_text==actual_text

#Verify Email input field
assert driver.find_element(By.ID,'ap_email').is_displayed()
driver.quit()