from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

driver.find_element(By.ID,'nav-link-accountList-nav-line-1').click()

expected_result= driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
actual_result=driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
assert expected_result==actual_result
print('Test case passed')
driver.quit()