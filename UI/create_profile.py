# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_profile.ui'
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
        MainWindow.resize(985, 594)
        MainWindow.setMinimumSize(QSize(985, 594))
        MainWindow.setMaximumSize(QSize(985, 594))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 431, 81))
        self.label.setStyleSheet(u"font: 700 48pt \"Microsoft JhengHei UI\";")
        self.label_full_name = QLabel(self.centralwidget)
        self.label_full_name.setObjectName(u"label_full_name")
        self.label_full_name.setGeometry(QRect(40, 110, 91, 41))
        self.label_full_name.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"")
        self.label_full_name_3 = QLabel(self.centralwidget)
        self.label_full_name_3.setObjectName(u"label_full_name_3")
        self.label_full_name_3.setGeometry(QRect(400, 110, 141, 41))
        self.label_full_name_3.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"")
        self.label_full_name_4 = QLabel(self.centralwidget)
        self.label_full_name_4.setObjectName(u"label_full_name_4")
        self.label_full_name_4.setGeometry(QRect(400, 200, 91, 41))
        self.label_full_name_4.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"")
        self.label_full_name_5 = QLabel(self.centralwidget)
        self.label_full_name_5.setObjectName(u"label_full_name_5")
        self.label_full_name_5.setGeometry(QRect(400, 370, 91, 41))
        self.label_full_name_5.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"")
        self.label_full_name_6 = QLabel(self.centralwidget)
        self.label_full_name_6.setObjectName(u"label_full_name_6")
        self.label_full_name_6.setGeometry(QRect(40, 190, 41, 41))
        self.label_full_name_6.setStyleSheet(u"font: 700 13pt \"Microsoft JhengHei UI\";\n"
"")
        self.radioButton_vaccinated = QRadioButton(self.centralwidget)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_vaccinated)
        self.radioButton_vaccinated.setObjectName(u"radioButton_vaccinated")
        self.radioButton_vaccinated.setGeometry(QRect(120, 120, 89, 20))
        self.radioButton_non_vaccinated = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.radioButton_non_vaccinated)
        self.radioButton_non_vaccinated.setObjectName(u"radioButton_non_vaccinated")
        self.radioButton_non_vaccinated.setGeometry(QRect(238, 120, 121, 20))
        self.textEdit_phone_number = QTextEdit(self.centralwidget)
        self.textEdit_phone_number.setObjectName(u"textEdit_phone_number")
        self.textEdit_phone_number.setGeometry(QRect(400, 150, 441, 31))
        self.textEdit_phone_number.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_phone_number.setInputMethodHints(Qt.ImhNone)
        self.textEdit_address = QTextEdit(self.centralwidget)
        self.textEdit_address.setObjectName(u"textEdit_address")
        self.textEdit_address.setGeometry(QRect(400, 240, 441, 111))
        self.textEdit_address.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_address.setInputMethodHints(Qt.ImhNone)
        self.textEdit_province = QTextEdit(self.centralwidget)
        self.textEdit_province.setObjectName(u"textEdit_province")
        self.textEdit_province.setGeometry(QRect(400, 410, 441, 31))
        self.textEdit_province.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_province.setInputMethodHints(Qt.ImhNone)
        self.textEdit_age = QTextEdit(self.centralwidget)
        self.textEdit_age.setObjectName(u"textEdit_age")
        self.textEdit_age.setGeometry(QRect(90, 200, 141, 31))
        self.textEdit_age.setStyleSheet(u"font: 700 12pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.textEdit_age.setInputMethodHints(Qt.ImhNone)
        self.pushButton_create = QPushButton(self.centralwidget)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(320, 500, 321, 41))
        self.pushButton_create.setStyleSheet(u"font: 700 16pt \"Microsoft JhengHei UI\";\n"
"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 260, 231, 251))
        self.label_2.setPixmap(QPixmap(u"create_virus2.png"))
        self.radioButton_dead = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.radioButton_dead)
        self.radioButton_dead.setObjectName(u"radioButton_dead")
        self.radioButton_dead.setGeometry(QRect(120, 150, 89, 20))
        self.radioButton_infected = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.radioButton_infected)
        self.radioButton_infected.setObjectName(u"radioButton_infected")
        self.radioButton_infected.setGeometry(QRect(240, 150, 89, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 985, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Create Profile", None))
        self.label_full_name.setText(QCoreApplication.translate("MainWindow", u"Stage", None))
        self.label_full_name_3.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.label_full_name_4.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_full_name_5.setText(QCoreApplication.translate("MainWindow", u"Province", None))
        self.label_full_name_6.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.radioButton_vaccinated.setText(QCoreApplication.translate("MainWindow", u"Vaccinated", None))
        self.radioButton_non_vaccinated.setText(QCoreApplication.translate("MainWindow", u"Non-vaccinated", None))
        self.textEdit_phone_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your phone number", None))
        self.textEdit_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your address", None))
        self.textEdit_province.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your province", None))
        self.textEdit_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your age", None))
        self.pushButton_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_2.setText("")
        self.radioButton_dead.setText(QCoreApplication.translate("MainWindow", u"Dead", None))
        self.radioButton_infected.setText(QCoreApplication.translate("MainWindow", u"Infected", None))
    # retranslateUi

