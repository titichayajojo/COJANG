# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Item2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(865, 300)
        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(110, 50, 616, 170))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QSize(0, 170))
        self.widget_5.setMaximumSize(QSize(16777215, 170))
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 218, 143);\n"
"border-radius: 15px;")
        self.label_39 = QLabel(self.widget_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 10, 111, 121))
        self.label_39.setStyleSheet(u"background-color: rgb(167, 167, 167);")
        self.layoutWidget_8 = QWidget(self.widget_5)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(130, 30, 101, 84))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.layoutWidget_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_11.addWidget(self.label_40)

        self.label_41 = QLabel(self.layoutWidget_8)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_11.addWidget(self.label_41)

        self.label_42 = QLabel(self.layoutWidget_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_11.addWidget(self.label_42)

        self.label_43 = QLabel(self.layoutWidget_8)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_11.addWidget(self.label_43)

        self.layoutWidget_9 = QWidget(self.widget_5)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(250, 30, 191, 86))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.layoutWidget_9)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_12.addWidget(self.label_44)

        self.label_45 = QLabel(self.layoutWidget_9)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_12.addWidget(self.label_45)

        self.label_46 = QLabel(self.layoutWidget_9)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_12.addWidget(self.label_46)

        self.label_47 = QLabel(self.layoutWidget_9)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_12.addWidget(self.label_47)

        self.groupBox = QGroupBox(self.widget_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(450, 20, 151, 101))
        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 20, 89, 20))
        self.radioButton_6 = QRadioButton(self.groupBox)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 40, 121, 20))
        self.radioButton_7 = QRadioButton(self.groupBox)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(10, 60, 89, 20))
        self.radioButton_8 = QRadioButton(self.groupBox)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(10, 80, 89, 20))
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 130, 111, 31))
        self.pushButton.setStyleSheet(u"font: 700 10pt \"Microsoft JhengHei UI\";\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 135, 65);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Surname", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"Tel", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"STATE", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"empty", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"STAGE", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"Vacinated", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"Non-Vacinated", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"Dead", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"Infected", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

