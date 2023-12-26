*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.globalsqa.com/demo-site/select-dropdown-menu/
${browser}  chrome
*** Test Cases ***
Dropdown & List Testing
    Open Browser  ${url}    ${browser}
    Maximize Browser Window
    
    Set Selenium Timeout    10 seconds
    Wait Until Page Contains    Home  #5 seconds timout by default. if you want it to wait more, set selenium timeout

    Select From List By Label  //select   Yemen
    Sleep    2
    Select From List By Value    //select   GNQ
    Sleep    2
    Select From List By Index    //select   0
    Sleep    2
