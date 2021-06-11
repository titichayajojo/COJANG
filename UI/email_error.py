# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_error.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(422, 243)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 351, 91))
        self.label.setStyleSheet(u"font: 700 20pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton_back = QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(140, 130, 131, 41))
        self.pushButton_back.setStyleSheet(u"font: 700 16pt \"Microsoft JhengHei UI\";\n"
"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"This email is already used", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
    # retranslateUi

