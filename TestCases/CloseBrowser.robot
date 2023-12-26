*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
CloseBrowser
    Open Browser  https://www.gmail.com  chrome
    Maximize Browser Window

    Open Browser  https://www.outlook.com  chrome
    Maximize Browser Window


    #Close Browser    #this closes the latest browser
    Close All Browsers
    #this closes the all browsers
