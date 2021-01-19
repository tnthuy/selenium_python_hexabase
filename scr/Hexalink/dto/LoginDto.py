from collections import namedtuple
from scr.Hexalink.util.excel_utils import ExcelFieldDto
import email

class AccountDto:
    def __init__(self, id, email, password):
        self.id=id
        self.email = email
        self.password = password

    # getter method
    def get_email(self):
        return self.id

    def setId(self, id):
        self.id = id
    
    def get_Email(self):
        return self.email
    
    def setEmail(self, email):
        self.email=email

    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password;
        
    def custom_dto_decoder(self):
        return namedtuple('AccountDto', self.keys())(*self.values())

    @staticmethod
    def excel_template():
        excel_field_dto_list = [ExcelFieldDto('ACCOUNT_ID', 'account_id'),
                                ExcelFieldDto('USERNAME', 'username'),
                                ExcelFieldDto('PASSWORD', 'password')]
        return excel_field_dto_list
    
    
