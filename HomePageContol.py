


from data import *
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
        self.m = DataManagement()
        self.STATE = "Bangkok"
        
        
    def addElement(self):
        
        # item = ItemController()
        people_set = self.m.getAllPeople()
        for i in people_set:
        
            person = people_set[i]
            if person['STATE'] == self.STATE:
                object = ItemController(person)
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
        provices = self.m.getAllProvice()
        for i in provices:
            self.ui.comboBox.addItem(i)
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_changed)

    def on_combobox_changed(self, value):
        print("combobox changed", value)
        self.STATE = value
        self.deleteElement()
        self.addElement()


    def deleteElement(self):
        for i in reversed(range(self.ui.verticalLayout.count())): 
            self.ui.verticalLayout.itemAt(i).widget().setParent(None)


  
    
    # do your code



            

        
       

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = HomePageContoller()
    home.addCombo()
    home.addElement()
    
    home.show()
    sys.exit(app.exec_())


