



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
    def __init__(self,person):
        QWidget.__init__(self,None)
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.person = person
        # print(self.person)
        self.ui.label_8.setText(self.person['fullname'])
        self.ui.label_9.setText(self.person['email'])
        self.ui.label_10.setText(self.person['province'])
        self.ui.label_11.setText(self.person['tel'])
        self.ui.label_12.setText(self.person['id_number'])
        self.ui.label_13.setText(self.person['nationality'])
    

    
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = DialogController()
    home.show()
    

