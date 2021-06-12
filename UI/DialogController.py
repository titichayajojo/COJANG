



from item3 import Item3

from os import stat

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from miniDialog import *

class DialogController(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Dialog()
        self.ui.setupUi(self)
    

    
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = DialogController()
    home.show()
    sys.exit(app.exec_())

