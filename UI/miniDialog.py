# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Dialog(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(48)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(300, 450))
        Form.setMaximumSize(QSize(300, 450))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 301, 451))
        self.widget.setStyleSheet(u"background-color: rgb(255, 161, 79);\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 111, 141))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 180, 161, 128))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 180, 63, 128))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_4)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_7)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"empty", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Province", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Telephone", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"ID card", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"nationality", None))
    # retranslateUi

