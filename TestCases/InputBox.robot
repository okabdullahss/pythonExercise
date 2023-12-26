*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome


*** Test Cases ***
TestingUnputBox
    Open Browser  ${url}  ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store
    Click Link    xpath://a[contains(text(),'Log in')]

    ${"element_txt"}  Set Variable  id:Email
    
    Element Should Be Enabled    ${"element_txt"}
    Element Should Be Visible    ${"element_txt"}

    Element Text Should Be    ${asdf}   haydaa

    Input Text    ${"element_txt"}    JesusChrist@mail.com
    Sleep    3
    Clear Element Text    ${"element_txt"}
    Sleep    1


*** Keywords ***