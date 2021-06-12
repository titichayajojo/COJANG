# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(985, 594)
        Login.setMinimumSize(QSize(985, 594))
        Login.setMaximumSize(QSize(985, 594))
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Login.setInputMethodHints(Qt.ImhNone)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_welcome_back = QLabel(self.centralwidget)
        self.label_welcome_back.setObjectName(u"label_welcome_back")
        self.label_welcome_back.setGeometry(QRect(230, -10, 491, 151))
        self.label_welcome_back.setStyleSheet(u"font: 700 48pt \"Microsoft JhengHei UI\";")
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(280, 130, 61, 41))
        self.label_email.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"color: rgb(159, 159, 159);")
        self.textEdit_email = QTextEdit(self.centralwidget)
        self.textEdit_email.setObjectName(u"textEdit_email")
        self.textEdit_email.setGeometry(QRect(280, 170, 441, 31))
        self.textEdit_email.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_email.setInputMethodHints(Qt.ImhNone)
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(280, 240, 91, 41))
        self.label_password.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"color: rgb(159, 159, 159);")
        self.textEdit_password = QTextEdit(self.centralwidget)
        self.textEdit_password.setObjectName(u"textEdit_password")
        self.textEdit_password.setGeometry(QRect(280, 280, 441, 31))
        self.textEdit_password.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";")
        self.textEdit_password.setInputMethodHints(Qt.ImhNone)
        self.pushButton_sign_in = QPushButton(self.centralwidget)
        self.pushButton_sign_in.setObjectName(u"pushButton_sign_in")
        self.pushButton_sign_in.setGeometry(QRect(330, 370, 321, 41))
        self.pushButton_sign_in.setStyleSheet(u"font: 700 16pt \"Microsoft JhengHei UI\";\n"
"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.label_covid_pic = QLabel(self.centralwidget)
        self.label_covid_pic.setObjectName(u"label_covid_pic")
        self.label_covid_pic.setGeometry(QRect(740, 10, 101, 101))
        self.label_covid_pic.setPixmap(QPixmap(u"c3.png"))
        self.label_sick_pic = QLabel(self.centralwidget)
        self.label_sick_pic.setObjectName(u"label_sick_pic")
        self.label_sick_pic.setGeometry(QRect(10, 330, 221, 241))
        self.label_sick_pic.setPixmap(QPixmap(u"p2.png"))
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 985, 22))
        Login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        Login.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_welcome_back.setText(QCoreApplication.translate("Login", u"Welcome back!", None))
        self.label_email.setText(QCoreApplication.translate("Login", u"Email", None))
        self.textEdit_email.setPlaceholderText(QCoreApplication.translate("Login", u"name@example.com", None))
        self.label_password.setText(QCoreApplication.translate("Login", u"Password", None))
        self.textEdit_password.setPlaceholderText(QCoreApplication.translate("Login", u"Enter your password", None))
        self.pushButton_sign_in.setText(QCoreApplication.translate("Login", u"Sign in!", None))
        self.label_covid_pic.setText("")
        self.label_sick_pic.setText("")
    # retranslateUi



if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QMainWindow()
        ui = Ui_Login()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())




