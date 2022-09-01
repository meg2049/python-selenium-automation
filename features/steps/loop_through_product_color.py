from selenium.webdriver.common.by import By
from behave import given, when, then

LIST_COLORS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors =['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray',
                      'Green', 'Khaki', 'Light-green', 'Pink', 'Purple', 'Red', 'Rose Red', 'White', 'Yellow' ]

    colors = context.driver.find_elements(*LIST_COLORS)
    print(colors)

    actual_colors = []

    for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        print('Actual_colors: ', actual_colors)

    assert expected_colors == actual_colors,f'Expected{expected_colors} but got {actual_colors}'
