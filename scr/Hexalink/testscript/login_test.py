import unittest
from selenium import webdriver

from scr.Hexalink.constant.constant import Constant
from scr.Hexalink.pages.login_page import LoginPage
from scr.Hexalink.library.get_data_login import get_csv_data

from ddt import ddt, data


@ddt
class Login(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\thuytn\git\python_Selenium\Browser\chromedriver.exe")
        # self.driver.implicitly_wait(30)
        # self.driver.maximize_window()

    @data(*get_csv_data('E:/CODE/Selenium_Python/inputdata/Login.csv'))
    def test_login(self, obj):
        driver = self.driver
        # navigate to the application home page
        driver.get(Constant.URL_AZ_HEXABASE)
        login_page = LoginPage(driver)
        login_page.input_data(obj.username, obj.password)
        login_page.click_login()

        # Check message

        has_error_message = login_page.show_LoginErrorMessage()
        if has_error_message:
            login = True
            message = login_page.getLoginErrorMessage()
            print(message)

        else:
            login = False
            print("tesst tesst")

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.TestCase()
