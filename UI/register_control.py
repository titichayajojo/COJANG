from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from register import Ui_register_2
from email_error_control import Email_Error
from login_control import Login
from create_profile_control import Create_Profile
from PySide6 import QtWidgets
from manipulateData import ManipulateData

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import pickle

class Register(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_register_2()
        self.ui.setupUi(self)
        self.ui.pushButton_sign_up.clicked.connect(self.sign_up_pressed)

    def sign_up_pressed(self):
        self.fullname = self.ui.textEdit_full_name.toPlainText()
        self.email = self.ui.textEdit_email.toPlainText()
        self.password = self.ui.textEdit_password.toPlainText()
        self.manipulateData = ManipulateData(self.fullname,self.email,self.password)
        self.loadData()
    
    def storeData(self):
        self.manipulateData.storeData()
    
    def loadData(self):
        check = self.manipulateData.loadData(self.email)
        if check == False:
            self.close()
            self.storeData() 


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        register = Register()
        register.show()
        sys.exit(app.exec_())

