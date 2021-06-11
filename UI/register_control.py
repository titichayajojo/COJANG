from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from register import Ui_register_2
from email_error_control import Email_Error
from login_control import Login
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import pickle

class Register(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_register_2()
        self.ui.setupUi(self)
        self.ui.pushButton_sign_up.clicked.connect(self.sign_up_pressed)

    def sign_up_pressed(self):
        self.fullname = self.ui.textEdit_full_name.toPlainText()
        self.email = self.ui.textEdit_email.toPlainText()
        self.password = self.ui.textEdit_password.toPlainText()
        self.loadData()

        
        
    
    def storeData(self):
        user = {'fullname' : self.fullname, 'email': self.email, 'password': self.password}
        # database
        db = {}
        print(user)
        db[str(self.email)] = user
        
        # Its important to use binary mode
        dbfile = open('users', 'ab')
        
        # source, destination
        pickle.dump(db, dbfile)                     
        dbfile.close()

        for dict in self.objs:
            for key in dict:
                print(key)

        self.close()
        self.login = Login()
        self.login.show()
        
    
    def loadData(self):
        self.email_error = Email_Error()
        self.objs = []
        checkUser = False
        f = open('users', 'rb')     
        while 1:
            try:
                self.objs.append(pickle.load(f))
            except EOFError:
                break

        for dict in self.objs:
            for key in dict:
                if key == self.email:
                    print("email is already used")
                    self.email_error.show()
                    checkUser = True

        if checkUser == False:
            self.storeData()
        

    

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        register = Register()
        register.show()
        sys.exit(app.exec_())
