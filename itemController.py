



from os import stat
from item import Item
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
        self.ui = Item()
        self.ui.setupUi(self)
        self.name = person['Name'] 
        self.surname = person['Surname']
        self.tel = person['Tel']
        self.state =  person['STATE']
        self.status = person['Status']

        self.ui.label_44.setText(self.name)
        self.ui.label_45.setText(self.surname)
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

        


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    home = ItemController()
    home.show()
    sys.exit(app.exec_())

