from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from admin_view import Ui_Admin_view
from profile_control import Profile_view
from login_control import Login
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
        f = open('users', 'rb')
        self.objs = pickle.load(f)
        self.name = self.ui.label_selected_name
        self.email = self.ui.label_selected_email
        self.tel = self.ui.label_selected_tel
        self.id = self.ui.label_selected_id
        self.nationality = self.ui.label_selected_nationality
        self.province = self.ui.label_selected_province
        self.age = self.ui.label_selected_age
        self.status = self.ui.label_status
        self.logout = self.ui.pushButton_log_out
        self.edit = self.ui.pushButton_edit_user
        self.edit.clicked.connect(self.edit_user)
        self.logout.clicked.connect(self.logout_user)

        self.vbox = QtWidgets.QVBoxLayout() 
        self.scroll = self.ui.scrollArea_all_user
        self.scrollWidget = self.ui.scrollAreaWidgetContents
        for i in self.objs:
            bt = QtWidgets.QPushButton(i)
            bt.setStyleSheet(u"font: 25 8pt \"Microsoft JhengHei UI Light\";\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border-radius: 5px;")
            bt.clicked.connect(self.user_pressed)
            self.vbox.addWidget(bt)

        self.scrollWidget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.scrollWidget)

    def user_pressed(self):
        
        self.name.setText("Name: " + self.objs[self.sender().text()]['fullname'])
        self.email.setText("Email: "+ self.objs[self.sender().text()]['email'])
        self.tel.setText("Tel: " + self.objs[self.sender().text()]['tel'])
        self.id.setText("ID: " + self.objs[self.sender().text()]['id_number'])
        self.nationality.setText("Nationality: " + self.objs[self.sender().text()]['nationality'])
        self.province.setText("Province: " + self.objs[self.sender().text()]['province'])
        self.age.setText("Age: " + self.objs[self.sender().text()]['age'])
        self.status.setText("Status: " + self.objs[self.sender().text()]['stage'])

    def edit_user(self):
        self.close()
        self.profile = Profile_view(self.email.text()[7:])
        self.profile.show()

    def logout_user(self):
        self.close()
        self.login = Login()
        self.login.show()




if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        admin = Admin_View()
        admin.show()
        sys.exit(app.exec_())

    

