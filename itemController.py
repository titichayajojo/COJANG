



from item import Item
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


class ItemController(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Item()
        self.ui.setupUi(self)

        
        
    
            
        
       

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = ItemController()
    home.show()
    sys.exit(app.exec_())

