# Created by MEGSAM-PC at 7/22/2022
Feature: Best Seller page functionality

  Scenario: Verify there are five links
    Given Open amazon.com page
    When Click on Best Sellers button
    Then Verify five links are shown