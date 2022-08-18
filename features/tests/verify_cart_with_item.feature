# Created by MEGSAM-PC at 7/22/2022
Feature: cart items verification

   Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for charger on amazon
    And Click on first product
    And Click on Add to cart button
    And click on cart menu
    Then Verify added item is in the Cart