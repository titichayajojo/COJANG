from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget
from profile_view import Ui_profile_view
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pickle
import sys

class Profile_view(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_profile_view()
        self.ui.setupUi(self)
        self.ui.pushButton_edit_profile.clicked.connect(self.edit)
        self.current = "Tee"

    def edit(self):
        self.objs = []
        f = open('users', 'rb')
        while 1:
            try:
                self.objs.append(pickle.load(f))
            except EOFError:
                break
        if(self.current in self.objs):
            self.objs[self.current]['fullname'] = self.ui.lineEdit_name
            self.objs[self.current]['email'] = self.ui.lineEdit_email
            ##self.objs[self.current]['tel'] = self.ui.lineEdit_tel
            ##self.objs[self.current]['province'] = self.ui.lineEdit_province
        with open('users.pickle', 'wb') as f:
            pickle.dump(self.objs, f)

        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        profile = Profile_view()
        profile.show()
        sys.exit(app.exec_())
