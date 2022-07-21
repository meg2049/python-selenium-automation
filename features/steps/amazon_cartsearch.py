from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amazon.com page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Cart menu')
def click_oncart_menu(context):
    context.driver.find_element(By.CSS_SELECTOR,'.nav-cart-icon.nav-sprite').click()


@then('You Amazon Cart is empty text shown')
def verify_result(context):
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_text == actual_text,f'Expected{expected_text},but got{actual_text}'