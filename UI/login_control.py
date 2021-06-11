from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from login import Ui_Login
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Login(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

    def sign_in_pressed(self):
        pass
    

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        login = Login()
        login.show()
        sys.exit(app.exec_())
