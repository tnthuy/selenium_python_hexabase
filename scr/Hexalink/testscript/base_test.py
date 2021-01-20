import os
import requests
import json
from datetime import datetime
import time

from src.Hexalink.constant.constant import Constant
from src.Hexxaconstant.url_constant import UrlConstant


class BaseTest(object):


    @staticmethod
    def get_current_time():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        return current_time

    def wait(self, timer):
        time.sleep(timer)

    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S_")
        return current_time
