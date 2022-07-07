from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')
# Amazon logo Search by XPATH, "//i[@class='a-icon a-icon-logo']"

# continue button search by ID,'continue'
# continue button search by XPATH,"//input[@id='continue']"


# Need help link search by XPATH,"//span[@class='a-expander-prompt']"


# Forgot your password link search by ID,'auth-fpp-link-bottom'
# Forgot your password link search by XPATH,"//a[@id='auth-fpp-link-bottom']"


# Other issues with sign in link search by ID,'ap-other-signin-issues-link'

# Other issues with sign in link search by XPATH, "//a[@id='ap-other-signin-issues-link']"


# create your Amazon account button Search by ID, 'createAccountSubmit'
# create your Amazon account button Search by XPATH, "//a[@id='createAccountSubmit']"


# privacy notice link Search by XPATH