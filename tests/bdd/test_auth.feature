Feature: Authentication

Scenario: Login user
  Given user exists
  When user logs in
  Then login is successful