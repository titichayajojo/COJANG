# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Welcome_page(object):
    def setupUi(self, Welcome_page):
        if not Welcome_page.objectName():
            Welcome_page.setObjectName(u"Welcome_page")
        Welcome_page.resize(985, 594)
        Welcome_page.setMinimumSize(QSize(985, 594))
        Welcome_page.setMaximumSize(QSize(985, 594))
        Welcome_page.setAutoFillBackground(False)
        Welcome_page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Welcome_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setGeometry(QRect(340, -20, 321, 111))
        self.label_welcome.setStyleSheet(u"font: 700 48pt \"Microsoft JhengHei UI \";")
        self.label_covid_pic = QLabel(self.centralwidget)
        self.label_covid_pic.setObjectName(u"label_covid_pic")
        self.label_covid_pic.setGeometry(QRect(350, 120, 691, 331))
        self.label_covid_pic.setMinimumSize(QSize(691, 0))
        self.label_covid_pic.setMaximumSize(QSize(691, 16777215))
        self.label_covid_pic.setPixmap(QPixmap(u"c300.png"))
        self.pushButton_sign_in = QPushButton(self.centralwidget)
        self.pushButton_sign_in.setObjectName(u"pushButton_sign_in")
        self.pushButton_sign_in.setGeometry(QRect(340, 460, 321, 41))
        self.pushButton_sign_in.setStyleSheet(u"font: 700 16pt \"Microsoft JhengHei UI\";\n"
"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.label_signin_info = QLabel(self.centralwidget)
        self.label_signin_info.setObjectName(u"label_signin_info")
        self.label_signin_info.setGeometry(QRect(370, 80, 251, 31))
        self.label_signin_info.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(159, 159, 159);")
        self.pushButton_sign_up = QPushButton(self.centralwidget)
        self.pushButton_sign_up.setObjectName(u"pushButton_sign_up")
        self.pushButton_sign_up.setGeometry(QRect(340, 510, 321, 41))
        self.pushButton_sign_up.setStyleSheet(u"font: 700 16pt \"Microsoft JhengHei UI\";\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(159, 159, 159);\n"
"color: rgb(255, 127, 23);")
        Welcome_page.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Welcome_page)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 985, 22))
        Welcome_page.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Welcome_page)
        self.statusbar.setObjectName(u"statusbar")
        Welcome_page.setStatusBar(self.statusbar)

        self.retranslateUi(Welcome_page)

        QMetaObject.connectSlotsByName(Welcome_page)
    # setupUi

    def retranslateUi(self, Welcome_page):
        Welcome_page.setWindowTitle(QCoreApplication.translate("Welcome_page", u"MainWindow", None))
        self.label_welcome.setText(QCoreApplication.translate("Welcome_page", u"Welcome!", None))
        self.label_covid_pic.setText("")
        self.pushButton_sign_in.setText(QCoreApplication.translate("Welcome_page", u"Sign in", None))
        self.label_signin_info.setText(QCoreApplication.translate("Welcome_page", u"Sign in or create a new account", None))
        self.pushButton_sign_up.setText(QCoreApplication.translate("Welcome_page", u"Sign up", None))
    # retranslateUi

