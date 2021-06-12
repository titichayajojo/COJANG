
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from create_profile import Ui_MainWindow
from manipulateData import ManipulateData
import currentUser
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

        self.vaccinated = self.ui.radioButton_vaccinated
        self.vaccinated.setChecked(True)

        self.non_vaccinated = self.ui.radioButton_non_vaccinated
        self.non_vaccinated.setChecked(True)

        self.dead = self.ui.radioButton_dead
        self.dead.setChecked(True)

        self.infected = self.ui.radioButton_infected
        self.infected.setChecked(True)
        
        self.manipulateData = ManipulateData()

        
        self.ui.pushButton_create.clicked.connect(self.create_pressed)

    def create_pressed(self):
        self.vaccinated.toggled.connect(self.radio_button_pressed(self.vaccinated))
        self.non_vaccinated.toggled.connect(self.radio_button_pressed(self.non_vaccinated))
        self.dead.toggled.connect(self.radio_button_pressed(self.dead))
        self.infected.toggled.connect(self.radio_button_pressed(self.infected))

        self.age = self.ui.textEdit_age.toPlainText()
        self.tel = self.ui.textEdit_phone_number.toPlainText()
        self.address = self.ui.textEdit_address.toPlainText()
        self.province = self.ui.textEdit_province.toPlainText()

        self.manipulateData.update_details(self.age,self.tel,self.address,self.province,currentUser.email)

        self.close()
    
    def radio_button_pressed(self,button):
        if button.text() == "Vaccinated":
            if button.isChecked() == True:
                #add vaccinated stage to db
                self.manipulateData.updateStage("Vaccinated",currentUser.email)

        elif button.text() == "Non-vaccinated":
            if button.isChecked() == True:
                #add Non-vaccinated stage to db
                self.manipulateData.updateStage("Non-vaccinated",currentUser.email)

        elif button.text() == "Dead":
            if button.isChecked() == True:
                #add Dead stage to db
                self.manipulateData.updateStage("Dead",currentUser.email)
        
        elif button.text() == "Infected":
            if button.isChecked() == True:
                #add Infected stage to db
                self.manipulateData.updateStage("Infected",currentUser.email)
              

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        create = Create_Profile()
        create.show()
        sys.exit(app.exec_())
