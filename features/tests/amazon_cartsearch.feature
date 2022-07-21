# Created by MEGSAM-PC at 7/21/2022\
Feature: Test Scenarios for Cart functionality

  Scenario: Verify that cart is empty
    Given Open amazon.com page
    When Click on Cart menu
    Then Your Amazon Cart is empty text shown