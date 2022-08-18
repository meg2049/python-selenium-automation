from selenium.webdriver.common.by import By
from behave import when, then


BEST_SELLERS_BUTTON = (By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
BEST_SELLERS_LINKS = (By.CSS_SELECTOR, '#zg_header a')


@when('Click on Best Sellers button')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS_BUTTON).click()


@then('Verify five links are shown')
def verify_links(context):
    links = context.driver.find_elements(*BEST_SELLERS_LINKS)
    print(links)
    print(type(links))
    assert len(links) == 5, f'Expected 5 links,but got (len(links))'
