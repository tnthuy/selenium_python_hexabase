import unittest
from selenium import webdriver

from scr.Hexalink.constant.constant import Constant
from scr.Hexalink.pages.login_page import LoginPage
from scr.Hexalink.library.GetDataLogin import get_csv_data

from ddt import ddt, data, unpack


@ddt
class Login(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\thuytn\git\python_Selenium\Browser\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @data(*get_csv_data('E:/CODE/Selenium_Python/inputdata/Login.csv'))
    def test_login(self, obj):
        driver = self.driver
        # navigate to the application home page
        driver.get(Constant.URL_AZ_HEXABASE)
        login_page = LoginPage(driver)
        login_page.input_data(obj.username, obj.password)
        login_page.click_login()

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.TestCase()
