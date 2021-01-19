import os
import requests
import json
from datetime import datetime
import time

from src.opcbiz.fxprimus.constant.constant import Constant
from src.opcbiz.fxprimus.constant.url_constant import UrlConstant


class BaseTest(object):
    api_gateway_url = 'https://apigateway.staging.k8s.fxprimus.tech/'

    @staticmethod
    def get_token():
        payload_login = {"username": "bach.nguyen+Ind@opcbiz.com",
                         "password": "Vmo@12345"}
        response = requests.post(UrlConstant.END_POINT_LOGIN_CLIENT, data=payload_login)
        json_token = json.loads(response.text)
        token = json_token['data']
        return token

    @staticmethod
    def get_client_token(username, password):
        payload_login = {"username": str(username),
                         "password": str(password)}
        response = requests.post(UrlConstant.END_POINT_LOGIN_CLIENT, data=payload_login)
        if str(response.status_code).startswith('2'):
            json_token = json.loads(response.text)
            token = json_token['data']
            return token
        else:
            mess = 'Code ' + str(response.status_code) + ': ' + Constant.CAN_NOT_LOGIN
            return mess

    @staticmethod
    def logged(token):
        if str(token).__contains__(Constant.CAN_NOT_LOGIN):
            return False
        else:
            return True

    @staticmethod
    def create_headers_bearer_auth(token):
        bearer_auth = "Bearer " + token
        headers = {"Authorization": bearer_auth}
        return headers

    @staticmethod
    def create_file_path_input(file_name_excel):
        current_directory = os.path.dirname(os.path.dirname(__file__))
        input_data_directory = os.path.join(current_directory.replace("\src\opcbiz\\fxprimus", ""), "inputData")
        file_path_excel = os.path.join(input_data_directory, file_name_excel)
        return file_path_excel

    @staticmethod
    def create_file_path_result(file_name_excel):
        current_directory = os.path.dirname(os.path.dirname(__file__))
        input_data_directory = os.path.join(current_directory.replace("\src\opcbiz\\fxprimus", ""), "report")
        file_path_excel = os.path.join(input_data_directory, file_name_excel)
        return file_path_excel

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
