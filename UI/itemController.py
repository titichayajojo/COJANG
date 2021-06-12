



from DialogController import DialogController
from item3 import Item3

from os import stat

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


class ItemController(QWidget):
    def __init__(self,person):
        QWidget.__init__(self,None)
        self.ui = Item3()
        self.ui.setupUi(self)
        self.person = person
        self.name = self.person['fullname'] 
       
        self.tel = self.person['tel']
        self.state =  self.person['province']
        self.status = self.person['stage']
        self.email = self.person['email']

        self.ui.label_44.setText(self.name)
        self.ui.label_45.setText(self.email)
        self.ui.label_46.setText(self.tel)
        self.ui.label_47.setText(self.state)

        


        if self.status == 'Vacinated':
            self.ui.radioButton_5.toggle()
            self.ui.radioButton_6.setEnabled(False)
            self.ui.radioButton_7.setEnabled(False)
            self.ui.radioButton_8.setEnabled(False)
        elif self.status == 'Non-Vacinated':
            self.ui.radioButton_6.toggle()
            self.ui.radioButton_5.setEnabled(False)
            self.ui.radioButton_7.setEnabled(False)
            self.ui.radioButton_8.setEnabled(False)
        elif self.status == 'Dead':
            self.ui.radioButton_7.toggle()
            self.ui.radioButton_5.setEnabled(False)
            self.ui.radioButton_6.setEnabled(False)
            self.ui.radioButton_8.setEnabled(False)
        else:
            self.ui.radioButton_8.toggle()
            self.ui.radioButton_5.setEnabled(False)
            self.ui.radioButton_6.setEnabled(False)
            self.ui.radioButton_7.setEnabled(False)
        
        self.ui.pushButton.clicked.connect(lambda: self.buttonOnClicked())
        pixmap = QPixmap('person2.png')
        self.ui.label_39.setPixmap(pixmap)
    def buttonOnClicked(self):
        self.dia = DialogController(self.person)
        self.dia.show()
       

        


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = ItemController()
    home.show()
    sys.exit(app.exec_())

