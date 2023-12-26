*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.globalsqa.com/demo-site/select-dropdown-menu/
${url2}  https://chercher.tech/practice/practice-dropdowns-selenium-webdriver
${browser}  chrome
*** Test Cases ***
Dropdown & List Testing
    Open Browser  ${url}    ${browser}
    Maximize Browser Window

    Select From List By Label  //select   Yemen
    Sleep    2
    Select From List By Value    //select   GNQ
    Sleep    2
    Select From List By Index    //select   0
    Sleep    2

DropdownList Test
    Open Browser  ${url2}    ${browser}

    Maximize Browser Window
   Set Selenium Speed    2 seconds
    ${speed}=  get selenium speed
   Log To Console    ${speed}

#selecting from list
    Select From List By Value    //select[@id='second']  burger
    Select From List By Index    //select[@id='second']  0
    Select From List By Label    //select[@id='second']  Donut
#unselecting from list
    Unselect From List By Label    //select[@id='second']  Burger
    Unselect From List By Value    //select[@id='second']   pizza
    Unselect From List By Index    //select[@id='second']   1


*** Keywords ***