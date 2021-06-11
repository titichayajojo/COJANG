from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from register import Ui_register_2
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Register(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_register_2()
        self.ui.setupUi(self)

        self.ui.


    

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        register = Register()
        register.show()
        sys.exit(app.exec_())
