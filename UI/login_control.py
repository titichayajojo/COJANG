from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from login import Ui_Login
from wrong_password_control import Wrong_password
from create_profile_control import Create_Profile
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import pickle

class Login(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_sign_in.clicked.connect(self.sign_in_pressed)

    def sign_in_pressed(self):
        self.email = self.ui.textEdit_email.toPlainText()
        self.password = self.ui.textEdit_password.toPlainText()
        self.loadData()

    def loadData(self):
        self.objs = []
        wrongEmailPassword = False
        f = open('users', 'rb')     
        while 1:
            try:
                self.objs.append(pickle.load(f))
            except EOFError:
                break

        for dict in self.objs:
            for key in dict:
                if key == self.email:
                    for value in dict[key]:
                        if value == 'password':
                            if dict[key][value] == self.password:
                                self.close()
                                self.create_profile = Create_Profile()
                                self.create_profile.show()
                                print("LOGIN")
                                return

        self.wrong_password = Wrong_password()
        self.wrong_password.show()


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        login = Login()
        login.show()
        sys.exit(app.exec_())
