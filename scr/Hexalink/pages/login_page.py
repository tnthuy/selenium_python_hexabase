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

    def click_forgotpass(self):
        link_forgotpassword_elt = self.find_element_by_xpath(locator.LoginPage.link_forgotPassword)
        self.click_wait(link_forgotpassword_elt, 1)

    def show_LoginErrorMessage(self):
        lct = locator.LoginPage.lbl_error
        flag = self.is_element_present_by_xpath(lct)
        if flag:
            return True
        else:
            return False

    def getLoginErrorMessage(self):
        if BasePage.is_element_present_by_xpath(locator.LoginPage.lbl_error):
            return self.get_text(locator.LoginPage.lbl_error)
        else:
            return " "
