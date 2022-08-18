from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@class='a-section a-spacing-none puis-padding-right-small s-title-instructions-style']/h2/a")
ADD_CART = (By.ID, 'add-to-cart-button')
VERIFY_RESULTS = (By.ID, 'sc-subtotal-label-activecart')
CART_MENU = (By.ID, 'nav-cart-count')
#DECLINE_WARRANTY = (By.ID, 'attachSiNoCoverage-announce')


@when('Click on first product')
def click_first_product(context):
    products = context.driver.find_elements(*PRODUCT_PRICE)
    products[0].click()


@when('click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_CART).click()
    sleep(10)

#@when('click no thanks for warranty')
#def click_no_to_thank(context):
    #context.driver.find_element(*DECLINE_WARRANTY).click()


@when('click on cart menu')
def click_on_cart_menu(context):
    context.driver.find_element(*CART_MENU).click()
    sleep(10)

@then('Verify added item is in the Cart')
def verify_result_cart(context):
    actual_text = 'Subtotal (1 item):'
    expected_text = context.driver.find_element(*VERIFY_RESULTS).text
    assert expected_text == actual_text, f'Expected{expected_text},but got{actual_text}'

