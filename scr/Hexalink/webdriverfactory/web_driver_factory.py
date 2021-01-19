
from scr.Hexalink.constant import constant  
from selenium import webdriver


class WebDriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == constant.Constant.CHROME:
            driver = webdriver.Chrome(
                executable_path=r'C:\Users\thuytn\git\webdrivers\chromedriver.exe')
        driver.implicitly_wait(30)
        return driver
