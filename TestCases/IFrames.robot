*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}
*** Test Cases ***
HandleFrameTest
    Open Browser    https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html  chrome
    Maximize Browser Window

    #select frame "frameName"
    #unselect frame  = goes back to previous frame and cancel the currently selected frame
     
    Select Frame    packageListFrame
    Sleep    2seconds
    Current Frame Should Contain    Packages
    Click Element    xpath://a[contains(text(),'org.openqa.selenium.mobile')]
    Unselect Frame
    Sleep    2seconds

    Select Frame    packageFrame
    Sleep    2seconds
    Current Frame Should Contain   NetworkConnection
    Click Element    xpath://span[contains(text(),'NetworkConnection')]
    Unselect Frame
    Sleep    2seconds

    Select Frame    classFrame
    Sleep    2seconds
    Current Frame Should Contain    All Known Implementing Classes:
    Sleep    2seconds
    Click Element    xpath://a[contains(text(),'ChromeDriver')]
    Sleep    2seconds
    Current Frame Should Contain    org.openqa.selenium.remote.RemoteWebDriver
    Sleep    2seconds
    Unselect Frame




    
    #Unselect Frame
    #Sleep    1seconds
    #Select Frame    packageFrame
    #${text}=    Get Text    xpath://span[contains(text(),'HasAuthentication')]
    #Log To Console    ${text}
    #Sleep    1seconds
    #Click Element    xpath://span[contains(text(),'TakesScreenshot')]
    #Sleep    2 seconds
    #Unselect Frame
    #Current Frame Should Contain    ALL CLASSES