*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}
*** Test Cases ***
HandleAlertTest
    Open Browser  https://testautomationpractice.blogspot.com/  chrome
    Click Element    xpath: //button[contains(text(),'Click Me')]
    Sleep    3seconds
    #Handle Alert  accept
    #Handle Alert  dismiss
    #Handle Alert  leave
 # handle alert leave command leaves the alert window as is.

    Alert Should Be Present  Press a button!
  # alert should be present string  command seeks the full string is present inside the alert or not.  Not the partial but as a whole of string
