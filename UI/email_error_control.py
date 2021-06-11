from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from email_error import Ui_MainWindow
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Email_Error(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_back.clicked.connect(self.back_pressed)

    def back_pressed(self):
        self.close()
    

