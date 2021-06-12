from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from admin_view import Ui_Admin_view
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pickle
import sys

class Admin_View(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Admin_view()
        self.ui.setupUi(self)