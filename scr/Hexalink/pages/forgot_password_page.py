# -*- coding: utf8 -*-


from scr.Hexalink.pages.base_page import BasePage
import scr.Hexalink.pages.locator as locator


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email):
        forgot_password_elt = self.find_element_by_xpath(locator.ForgotPasswordPage.input_emailForgot)
        self.send_key(forgot_password_elt, email)

    def click_forgot_pass(self):
        btn_forgot_pass_elt = self.find_element_by_xpath(locator.ForgotPasswordPage.btn_passwordReset)
        self.click_wait(btn_forgot_pass_elt, 1)
