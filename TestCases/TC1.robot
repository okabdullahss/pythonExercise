*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
LoginTest
   Open Browser  ${url}  ${browser}
   loginToApplication
   Close Browser

*** Keywords ***
loginToApplication
   Click Link    xpath://a[contains(text(),'Log in')]
   Input Text    id:Email  pavonaltrainning@gmail.com
   Input Text    id:Password  Test@123
   Click Element    xpath://button[contains(text(),'Log in')]
