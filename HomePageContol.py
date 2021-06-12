


from itemController import ItemController
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


import sys
from board3 import *


class HomePageContoller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
    def addElement(self):
        
        # item = ItemController()
        for i in range(20):
            object = ItemController()
            object.setObjectName(u"widget_5")
            object.setGeometry(QRect(140, 80, 616, 150))
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
           
            sizePolicy.setHeightForWidth(object.sizePolicy().hasHeightForWidth())
            object.setSizePolicy(sizePolicy)
            object.setMinimumSize(QSize(0, 230))
            object.setStyleSheet(u"background-color: rgb(255, 218, 143);\n"
"border-radius: 15px;")
           
           
            self.ui.verticalLayout.addWidget(object)
    
    def addCombo(self):
        self.ui.comboBox.addItem("Yes")
            

        
       

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = HomePageContoller()
    home.addElement()
    home.addCombo()
    home.show()
    sys.exit(app.exec_())

