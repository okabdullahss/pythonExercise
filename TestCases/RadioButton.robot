*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demoqa.com/automation-practice-form
${browser}  chrome

*** Test Cases ***
Testing Radio Button
       Open Browser  ${url}  ${browser}
       Maximize Browser Window
       Set Selenium Speed    1seconds  #this will wait 1 seconds between every command

       #Select Radio Button    gender    Male   |
       #Select Checkbox    Sports               |    these didnt work. so i clicked elements, instead of selecting
       #Unselect Checkbox    Sports             |

       Click Element    xpath://label[contains(text(),'Male')]
       Click Element    xpath://label[contains(text(),'Female')]
       Click Element    xpath://label[contains(text(),'Sports')]
       Click Element    xpath://label[contains(text(),'Reading')]
       Click Element    xpath://label[contains(text(),'Sports')]
       Click Element    xpath://label[contains(text(),'Reading')]

        

*** Keywords ***


