*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.globalsqa.com/demo-site/select-dropdown-menu/
${browser}  chrome
*** Test Cases ***
Dropdown & List Testing
    Open Browser  ${url}    ${browser}
    Maximize Browser Window
    
    ${implicitSpeed}=  Get Selenium Implicit Wait
    Log To Console    ${implicitSpeed}

    Set Selenium Implicit Wait  10 seconds
    ${implicitSpeed}=  Get Selenium Implicit Wait
    Log To Console    ${implicitSpeed}

    Select From List By Label  //select1   Yemen  # //select1 is intentionally mistyped so that implicit wait is run
    Select From List By Value    //select   GNQ
    Select From List By Index    //select   0
