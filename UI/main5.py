# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main5.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainPage(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1200, 700))
        Form.setMaximumSize(QSize(1200, 700))
        self.widget = QWidget(Form)
        self.widget.setMinimumSize(QSize(1200, 700))
        self.widget.setMaximumSize(QSize(1200, 700))
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1001, 1000))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"background-color: rgb(255, 161, 79);")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 301, 581))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 160, 281, 411))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 161, 79);")
        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 30, 251, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 251, 16))
        self.label_6.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 230, 261, 171))
        self.widget_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.groupBox_2 = QGroupBox(self.widget_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 241, 131))
        self.radioButton_10 = QRadioButton(self.groupBox_2)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setGeometry(QRect(20, 30, 89, 20))
        self.radioButton_12 = QRadioButton(self.groupBox_2)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(20, 70, 89, 20))
        self.radioButton_11 = QRadioButton(self.groupBox_2)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setGeometry(QRect(20, 50, 121, 20))
        self.radioButton_9 = QRadioButton(self.groupBox_2)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setGeometry(QRect(20, 90, 89, 20))
        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 60, 261, 161))
        self.widget_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.layoutWidget = QWidget(self.widget_8)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 91, 106))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_5)

        self.layoutWidget1 = QWidget(self.widget_8)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 30, 161, 106))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_10)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 141))
        self.label.setStyleSheet(u"background-color: rgb(255, 161, 79);")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"PushButton")
        self.pushButton.setGeometry(QRect(160, 110, 111, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 110, 62);")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setMinimumSize(QSize(860, 680))
        self.widget_4.setMaximumSize(QSize(860, 680))
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(320, 10, 671, 581))
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.scrollArea = QScrollArea(self.widget_4)
        self.scrollArea.setMinimumSize(QSize(840, 600))
        self.scrollArea.setMaximumSize(QSize(840, 600))
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 60, 500, 1000))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 483, 1000))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textEdit = QTextEdit(self.widget_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 10, 571, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"font: 12pt \"Segoe UI\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Select Province", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"STAGE CHECK", None))
        self.radioButton_10.setText(QCoreApplication.translate("Form", u"Vacinated", None))
        self.radioButton_12.setText(QCoreApplication.translate("Form", u"Dead", None))
        self.radioButton_11.setText(QCoreApplication.translate("Form", u"Non-Vacinated", None))
        self.radioButton_9.setText(QCoreApplication.translate("Form", u"Infected", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"   Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"   Surname", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"   Province", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"   Tel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Edit Profile", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
    # retranslateUi

