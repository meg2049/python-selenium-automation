
from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

SUB_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

@given('open amazon bestsellers url')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/BestSellers/')
    sleep(2)

@when('User can click through all sub links and verify that correct page open')
def click_through_toplinks_and_verify_pages(context):
    top_links = context.driver.find_elements(*SUB_LINKS)
    print(SUB_LINKS)

    for i in range(len(SUB_LINKS)):
        link_to_click = context.driver.find_elements(*SUB_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()
        sleep(2)
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} but got {header_text}'