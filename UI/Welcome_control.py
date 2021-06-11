from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from Welcome import Ui_Welcome_page
from login_control import Login
from register_control import Register
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Welcome(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Welcome_page()
        self.ui.setupUi(self)
        self.ui.pushButton_sign_in.clicked.connect(self.sign_in_pressed)
        self.ui.pushButton_sign_up.clicked.connect(self.sign_up_pressed)
    
    def sign_in_pressed(self):
        self.close()
        self.login = Login()
        self.login.show()

    def sign_up_pressed(self):
        self.close()
        self.register = Register()
        self.register.show()  

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        welcome = Welcome()
        welcome.show()
        sys.exit(app.exec_())
