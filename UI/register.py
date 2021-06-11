# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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


class Ui_register_2(object):
    def setupUi(self, register_2):
        if not register_2.objectName():
            register_2.setObjectName(u"register_2")
        register_2.resize(985, 594)
        register_2.setMinimumSize(QSize(985, 594))
        register_2.setMaximumSize(QSize(985, 594))
        register_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(register_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_create_new_account = QLabel(self.centralwidget)
        self.label_create_new_account.setObjectName(u"label_create_new_account")
        self.label_create_new_account.setGeometry(QRect(170, -10, 661, 151))
        self.label_create_new_account.setStyleSheet(u"font: 700 48pt \"Microsoft JhengHei UI\";")
        self.label_full_name = QLabel(self.centralwidget)
        self.label_full_name.setObjectName(u"label_full_name")
        self.label_full_name.setGeometry(QRect(280, 150, 91, 41))
        self.label_full_name.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"color: rgb(159, 159, 159);")
        self.textEdit_full_name = QTextEdit(self.centralwidget)
        self.textEdit_full_name.setObjectName(u"textEdit_full_name")
        self.textEdit_full_name.setGeometry(QRect(280, 190, 441, 31))
        self.textEdit_full_name.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_full_name.setInputMethodHints(Qt.ImhNone)
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(280, 240, 161, 41))
        self.label_email.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"color: rgb(159, 159, 159);")
        self.textEdit_email = QTextEdit(self.centralwidget)
        self.textEdit_email.setObjectName(u"textEdit_email")
        self.textEdit_email.setGeometry(QRect(280, 280, 441, 31))
        self.textEdit_email.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_email.setInputMethodHints(Qt.ImhNone)
        self.label_create_password = QLabel(self.centralwidget)
        self.label_create_password.setObjectName(u"label_create_password")
        self.label_create_password.setGeometry(QRect(280, 330, 161, 41))
        self.label_create_password.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"color: rgb(159, 159, 159);")
        self.textEdit_password = QTextEdit(self.centralwidget)
        self.textEdit_password.setObjectName(u"textEdit_password")
        self.textEdit_password.setGeometry(QRect(280, 370, 441, 31))
        self.textEdit_password.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_password.setInputMethodHints(Qt.ImhNone)
        self.pushButton_sign_up = QPushButton(self.centralwidget)
        self.pushButton_sign_up.setObjectName(u"pushButton_sign_up")
        self.pushButton_sign_up.setGeometry(QRect(320, 470, 321, 41))
        self.pushButton_sign_up.setStyleSheet(u"font: 700 16pt \"Microsoft JhengHei UI\";\n"
"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.label_injection_pic = QLabel(self.centralwidget)
        self.label_injection_pic.setObjectName(u"label_injection_pic")
        self.label_injection_pic.setGeometry(QRect(20, 320, 231, 221))
        self.label_injection_pic.setPixmap(QPixmap(u"pics/injection2.jpg"))
        self.label_virus_pic = QLabel(self.centralwidget)
        self.label_virus_pic.setObjectName(u"label_virus_pic")
        self.label_virus_pic.setGeometry(QRect(800, 200, 121, 131))
        self.label_virus_pic.setPixmap(QPixmap(u"pics/virus2.png"))
        register_2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(register_2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 985, 22))
        register_2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(register_2)
        self.statusbar.setObjectName(u"statusbar")
        register_2.setStatusBar(self.statusbar)

        self.retranslateUi(register_2)

        QMetaObject.connectSlotsByName(register_2)
    # setupUi

    def retranslateUi(self, register_2):
        register_2.setWindowTitle(QCoreApplication.translate("register_2", u"MainWindow", None))
        self.label_create_new_account.setText(QCoreApplication.translate("register_2", u"Create New Account", None))
        self.label_full_name.setText(QCoreApplication.translate("register_2", u"Full name", None))
        self.textEdit_full_name.setPlaceholderText(QCoreApplication.translate("register_2", u"Enter your name", None))
        self.label_email.setText(QCoreApplication.translate("register_2", u"Email address", None))
        self.textEdit_email.setPlaceholderText(QCoreApplication.translate("register_2", u"name@example.com", None))
        self.label_create_password.setText(QCoreApplication.translate("register_2", u"Create password", None))
        self.textEdit_password.setPlaceholderText(QCoreApplication.translate("register_2", u"Enter your password", None))
        self.pushButton_sign_up.setText(QCoreApplication.translate("register_2", u"Sign up!", None))
        self.label_injection_pic.setText("")
        self.label_virus_pic.setText("")
    # retranslateUi

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QMainWindow()
        ui = Ui_register_2()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
