# Created by MEGSAM-PC at 7/1/2022
Feature: Test Scenarios for search Functionality
  # Enter feature description here

  Scenario: User can search for product
    Given open Google page
    When Input Watches into search field
    And click on search icon
    Then product result for watches are shown