from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from profile_view import Ui_profile_view
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import currentUser
import pickle
import sys

class Profile_view(QMainWindow):
    # class constructor
    def __init__(self, current, last):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_profile_view()
        self.ui.setupUi(self)
        self.ui.pushButton_edit_profile.clicked.connect(self.edit)
        self.vaccinated = self.ui.radioButton_vaccinated
        self.non_vaccinated = self.ui.radioButton_n_vaccinated
        self.dead = self.ui.radioButton_death
        self.infected= self.ui.radioButton_infected
        self.current = current
        self.last = last
        self.ui.label_email.setText(self.current)

    def radio_button_pressed(self,button):
            if button.isChecked() == True:
                #add vaccinated stage to db
                return button.text()
            else:
                return False
    def edit(self):
        vacc = self.radio_button_pressed(self.vaccinated)
        nvacc = self.radio_button_pressed(self.non_vaccinated)
        death = self.radio_button_pressed(self.dead)
        infec = self.radio_button_pressed(self.infected)
        f = open('users', 'rb')
        self.objs = pickle.load(f)
        f.close()
        if(self.current in self.objs):
            self.objs[self.current]['fullname'] = self.ui.lineEdit_name.text()
            self.objs[self.current]['age'] = self.ui.lineEdit_age.text()
            self.objs[self.current]['nationality'] = self.ui.lineEdit_nationality.text()
            self.objs[self.current]['tel'] = self.ui.lineEdit_tel.text()
            self.objs[self.current]['id_number'] = self.ui.lineEdit_id.text()
            self.objs[self.current]['province'] = self.ui.lineEdit_province.text()
            if(vacc):
                self.objs[self.current]['stage'] = vacc
            elif(nvacc):
                self.objs[self.current]['stage'] = nvacc
            elif(death):
                self.objs[self.current]['stage'] = death
            elif(infec):
                self.objs[self.current]['stage'] = infec
        with open('users', 'wb') as f:
            pickle.dump(self.objs, f)
        print(self.objs[self.current])
        self.close()
        if(currentUser.email != 'admin@hotmail.com'):
            self.last.setCurrentProfile(self.objs[self.current])
            self.last.show()
        else:
            self.last.update_user(self.objs[self.current])
            self.last.show()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        profile = Profile_view("hello@hotmail.com")
        profile.show()
        sys.exit(app.exec_())

        