from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

driver.find_element(By.ID,'nav-orders').click()

expected_result= driver.find_element(By.XPATH,"//div[@class='a-row a-spacing-base']")
actual_result= driver.find_element(By.XPATH,"//div[@class='a-row a-spacing-base']")
assert expected_result==actual_result

print('Test cases passed')
driver.quit()
