from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from create_profile import Ui_MainWindow
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Create_Profile(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_create.clicked.connect(self.create_pressed)

    def create_pressed(self):
        self.close()
    

