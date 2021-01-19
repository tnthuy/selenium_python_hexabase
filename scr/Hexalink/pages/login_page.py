# !/usr/bin/env python
# -*- coding: utf8 -*-


from scr.Hexalink.pages.base_page import BasePage
import scr.Hexalink.pages.locator as locator


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def input_data(self, username, password):
        locatorx = locator.LoginPage.input_email
        username_elt = self.find_element_by_xpath(locatorx)
        self.send_key(username_elt, username)

        password_elt = self.find_element_by_xpath(locator.LoginPage.input_password)
        self.send_key(password_elt, password)

    def click_login(self):
        btn_login_elt = self.find_element_by_xpath(locator.LoginPage.btn_signin)
        self.click_wait(btn_login_elt, 1)


    # def test_Login(self, ID, EMAIL, PASSWORD):
    #     self.username = self.driver.find_element_by_xpath(LoginPage.input_email)
    #     self.username.send_keys(EMAIL)
    #     # Enter pass
    #     self.password = self.driver.find_element_by_xpath(LoginPage.input_password)
    #     self.password.send_keys(PASSWORD)
    #     self.driver.implicitly_wait(3000)
    #
    #     # Click Login button
    #     self.driver.find_element_by_xpath(LoginPage.btn_signin).click()

    # def test_ClickForgotPassword(self):
    #     self.forgotPassword = self.driver.find_element_by_xpath(LoginPage.link_forgotPassword)
    #     self.forgotPassword.click()
