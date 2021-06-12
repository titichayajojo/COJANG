# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_view.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_profile_view(object):
    def setupUi(self, profile_view):
        if not profile_view.objectName():
            profile_view.setObjectName(u"profile_view")
        profile_view.resize(985, 594)
        profile_view.setMinimumSize(QSize(985, 594))
        profile_view.setMaximumSize(QSize(985, 594))
        profile_view.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.label = QLabel(profile_view)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 10, 121, 111))
        self.label.setPixmap(QPixmap(u"../noprofile3.png"))
        self.label_name = QLabel(profile_view)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(410, 170, 161, 16))
        self.label_name.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_email = QLabel(profile_view)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(440, 130, 161, 16))
        self.label_email.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.pushButton_edit_profile = QPushButton(profile_view)
        self.pushButton_edit_profile.setObjectName(u"pushButton_edit_profile")
        self.pushButton_edit_profile.setGeometry(QRect(450, 520, 181, 41))
        self.pushButton_edit_profile.setStyleSheet(u"border-radius: 15px;\n"
"font: 25 8pt \"Microsoft JhengHei UI Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_status_prompt = QLabel(profile_view)
        self.label_status_prompt.setObjectName(u"label_status_prompt")
        self.label_status_prompt.setGeometry(QRect(470, 480, 61, 16))
        self.label_status_prompt.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_status = QLabel(profile_view)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(540, 480, 161, 16))
        self.label_status.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_tel = QLabel(profile_view)
        self.label_tel.setObjectName(u"label_tel")
        self.label_tel.setGeometry(QRect(410, 210, 161, 16))
        self.label_tel.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.doctor = QLabel(profile_view)
        self.doctor.setObjectName(u"doctor")
        self.doctor.setGeometry(QRect(210, 180, 91, 181))
        self.doctor.setPixmap(QPixmap(u"../doc1.png"))
        self.label_province = QLabel(profile_view)
        self.label_province.setObjectName(u"label_province")
        self.label_province.setGeometry(QRect(410, 250, 161, 16))
        self.label_province.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.lineEdit_name = QLineEdit(profile_view)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(510, 170, 161, 21))
        self.lineEdit_name.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_tel = QLineEdit(profile_view)
        self.lineEdit_tel.setObjectName(u"lineEdit_tel")
        self.lineEdit_tel.setGeometry(QRect(510, 210, 161, 21))
        self.lineEdit_tel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_province = QLineEdit(profile_view)
        self.lineEdit_province.setObjectName(u"lineEdit_province")
        self.lineEdit_province.setGeometry(QRect(510, 250, 161, 21))
        self.lineEdit_province.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_id = QLineEdit(profile_view)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(510, 290, 161, 21))
        self.lineEdit_id.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(0, 0, 0);")
        self.id = QLabel(profile_view)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(410, 290, 161, 16))
        self.id.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.lineEdit_age = QLineEdit(profile_view)
        self.lineEdit_age.setObjectName(u"lineEdit_age")
        self.lineEdit_age.setGeometry(QRect(510, 330, 161, 21))
        self.lineEdit_age.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(0, 0, 0);")
        self.label_age = QLabel(profile_view)
        self.label_age.setObjectName(u"label_age")
        self.label_age.setGeometry(QRect(410, 320, 161, 31))
        self.label_age.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.lineEdit_nationality = QLineEdit(profile_view)
        self.lineEdit_nationality.setObjectName(u"lineEdit_nationality")
        self.lineEdit_nationality.setGeometry(QRect(510, 370, 161, 21))
        self.lineEdit_nationality.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(0, 0, 0);")
        self.label_nationality = QLabel(profile_view)
        self.label_nationality.setObjectName(u"label_nationality")
        self.label_nationality.setGeometry(QRect(410, 370, 161, 16))
        self.label_nationality.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.layoutWidget = QWidget(profile_view)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 440, 464, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_n_vaccinated = QRadioButton(self.layoutWidget)
        self.radioButton_n_vaccinated.setObjectName(u"radioButton_n_vaccinated")
        self.radioButton_n_vaccinated.setStyleSheet(u"\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";")

        self.horizontalLayout.addWidget(self.radioButton_n_vaccinated)

        self.radioButton_vaccinated = QRadioButton(self.layoutWidget)
        self.radioButton_vaccinated.setObjectName(u"radioButton_vaccinated")
        self.radioButton_vaccinated.setStyleSheet(u"\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";")

        self.horizontalLayout.addWidget(self.radioButton_vaccinated)

        self.radioButton_infected = QRadioButton(self.layoutWidget)
        self.radioButton_infected.setObjectName(u"radioButton_infected")
        self.radioButton_infected.setStyleSheet(u"\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";")

        self.horizontalLayout.addWidget(self.radioButton_infected)

        self.radioButton_death = QRadioButton(self.layoutWidget)
        self.radioButton_death.setObjectName(u"radioButton_death")
        self.radioButton_death.setStyleSheet(u"\n"
"font: 290 14pt \"Microsoft JhengHei UI Light\";")

        self.horizontalLayout.addWidget(self.radioButton_death)

        self.layoutWidget.raise_()
        self.label.raise_()
        self.label_name.raise_()
        self.label_email.raise_()
        self.pushButton_edit_profile.raise_()
        self.label_status_prompt.raise_()
        self.label_status.raise_()
        self.label_tel.raise_()
        self.doctor.raise_()
        self.label_province.raise_()
        self.id.raise_()
        self.lineEdit_name.raise_()
        self.lineEdit_tel.raise_()
        self.lineEdit_province.raise_()
        self.lineEdit_id.raise_()
        self.label_age.raise_()
        self.lineEdit_age.raise_()
        self.label_nationality.raise_()
        self.lineEdit_nationality.raise_()

        self.retranslateUi(profile_view)

        QMetaObject.connectSlotsByName(profile_view)
    # setupUi

    def retranslateUi(self, profile_view):
        profile_view.setWindowTitle(QCoreApplication.translate("profile_view", u"Form", None))
        self.label.setText("")
        self.label_name.setText(QCoreApplication.translate("profile_view", u"Name", None))
        self.label_email.setText(QCoreApplication.translate("profile_view", u"Email", None))
        self.pushButton_edit_profile.setText(QCoreApplication.translate("profile_view", u"Edit Profile", None))
        self.label_status_prompt.setText(QCoreApplication.translate("profile_view", u"Status:", None))
        self.label_status.setText(QCoreApplication.translate("profile_view", u"Infected?", None))
        self.label_tel.setText(QCoreApplication.translate("profile_view", u"Tel", None))
        self.doctor.setText("")
        self.label_province.setText(QCoreApplication.translate("profile_view", u"Province", None))
        self.id.setText(QCoreApplication.translate("profile_view", u"ID", None))
        self.label_age.setText(QCoreApplication.translate("profile_view", u"Age", None))
        self.label_nationality.setText(QCoreApplication.translate("profile_view", u"Nationality", None))
        self.radioButton_n_vaccinated.setText(QCoreApplication.translate("profile_view", u"Non-Vaccinated", None))
        self.radioButton_vaccinated.setText(QCoreApplication.translate("profile_view", u"Vaccinated", None))
        self.radioButton_infected.setText(QCoreApplication.translate("profile_view", u"Infected", None))
        self.radioButton_death.setText(QCoreApplication.translate("profile_view", u"Death", None))
    # retranslateUi

