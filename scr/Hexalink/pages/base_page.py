from datetime import datetime
import time
from selenium.common import exceptions


class BasePage(object):

    # find_element
    # @staticmethod
    def __init__(self, diver):
        self.driver = diver

    def find_element_by_id(self, locator_id):
        return self.driver.find_element_by_id(locator_id)

    # @staticmethod
    def find_element_by_xpath(self, locator_xpath):
        return self.driver.find_element_by_xpath(locator_xpath)

    # @staticmethod
    def find_element_by_name(self, locator_name):
        return self.driver.find_element_by_name(locator_name)

    # Actions - Clicks
    # @staticmethod
    def wait_click(self, element, timer):
        time.sleep(timer)
        element.click()

    # @staticmethod
    def click_wait(self, element, timer):
        element.click()
        time.sleep(timer)

    # @staticmethod
    def click(self, element):
        element.click()

    # Actions - Send key
    # @staticmethod
    def send_key(self, element, keys_to_send):
        # web_element = WebElement(element)
        element.send_keys(keys_to_send)

    def get_text(self, element):
        return element.text()

    def waiting(self, timer):
        print("Waiting: {}".format(timer))
        time.sleep(timer)

    def is_element_present_by_xpath(self, xpath):
        try:
            self.find_element_by_xpath(xpath)
            print("is_element_present_by_xpath: " + xpath);
            return True
        except exceptions.NoSuchElementException:
            print("NoSuchElementException")
            return False

    def is_element_present_by_id(self, element_id):
        try:
            self.find_element_by_id(element_id)
            print("is_element_present_by_xpath: " + element_id);
            return True
        except exceptions.NoSuchElementException:
            print("NoSuchElementException")
            return False

    def logout(self):
        header_username_link = self.find_element_by_id("header-username")
        self.click_wait(header_username_link, 1)
        logout_element = self.find_element_by_id("logout-link-text")
        self.click(logout_element)
        print("logout")

    def create_new_email(self):
        now = datetime.now()
        current_time = now.strftime("%d%m%y%H%M%S")
        new_email = 'lqa-tester+'+current_time+'@b-eee.com'
        return new_email
