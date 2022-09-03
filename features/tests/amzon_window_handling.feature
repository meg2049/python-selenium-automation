# Created by MEGSAM-PC at 9/1/2022
Feature: User can test window handling

 Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon Terms & Conditions page
    When Store original window
    And Click on Privacy Notice link
    And Switch to newly opened window
    Then Verify Amazon Privacy Notice page opened
    And User can close new window & switch back to original

