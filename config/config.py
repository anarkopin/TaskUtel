from selenium import webdriver

def driver():
    #drive chrome
    driver = webdriver.Chrome("webdriver//chromedriver.exe")
    driver.implicitly_wait(20)
    #abrir pagina
    return driver


