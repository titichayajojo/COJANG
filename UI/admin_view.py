# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_view3.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Admin_view(object):
    def setupUi(self, Admin_view):
        if not Admin_view.objectName():
            Admin_view.setObjectName(u"Admin_view")
        Admin_view.resize(985, 594)
        Admin_view.setMinimumSize(QSize(985, 594))
        Admin_view.setMaximumSize(QSize(985, 594))
        Admin_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_status = QLabel(Admin_view)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(630, 320, 151, 16))
        self.label_status.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.pushButton_edit_user = QPushButton(Admin_view)
        self.pushButton_edit_user.setObjectName(u"pushButton_edit_user")
        self.pushButton_edit_user.setGeometry(QRect(780, 350, 61, 23))
        self.pushButton_edit_user.setStyleSheet(u"font: 25 8pt \"Microsoft JhengHei UI Light\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 4px;")
        self.label_selected_province = QLabel(Admin_view)
        self.label_selected_province.setObjectName(u"label_selected_province")
        self.label_selected_province.setGeometry(QRect(630, 220, 211, 21))
        self.label_selected_province.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.scrollArea_all_user = QScrollArea(Admin_view)
        self.scrollArea_all_user.setObjectName(u"scrollArea_all_user")
        self.scrollArea_all_user.setGeometry(QRect(9, 9, 611, 581))
        self.scrollArea_all_user.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.scrollArea_all_user.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 579))
        self.scrollArea_all_user.setWidget(self.scrollAreaWidgetContents)
        self.label_selected_age = QLabel(Admin_view)
        self.label_selected_age.setObjectName(u"label_selected_age")
        self.label_selected_age.setGeometry(QRect(630, 260, 211, 31))
        self.label_selected_age.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_selected_nationality = QLabel(Admin_view)
        self.label_selected_nationality.setObjectName(u"label_selected_nationality")
        self.label_selected_nationality.setGeometry(QRect(630, 170, 211, 31))
        self.label_selected_nationality.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_selected_tel = QLabel(Admin_view)
        self.label_selected_tel.setObjectName(u"label_selected_tel")
        self.label_selected_tel.setGeometry(QRect(630, 50, 211, 31))
        self.label_selected_tel.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_selected_name = QLabel(Admin_view)
        self.label_selected_name.setObjectName(u"label_selected_name")
        self.label_selected_name.setGeometry(QRect(630, 100, 211, 16))
        self.label_selected_name.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_selected_email = QLabel(Admin_view)
        self.label_selected_email.setObjectName(u"label_selected_email")
        self.label_selected_email.setGeometry(QRect(630, 10, 211, 21))
        self.label_selected_email.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label_selected_id = QLabel(Admin_view)
        self.label_selected_id.setObjectName(u"label_selected_id")
        self.label_selected_id.setGeometry(QRect(630, 140, 211, 16))
        self.label_selected_id.setStyleSheet(u"font: 25 14pt \"Microsoft JhengHei UI Light\";")
        self.label = QLabel(Admin_view)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(780, 420, 111, 151))
        self.label.setPixmap(QPixmap(u"../doc1.png"))

        self.retranslateUi(Admin_view)

        QMetaObject.connectSlotsByName(Admin_view)
    # setupUi

    def retranslateUi(self, Admin_view):
        Admin_view.setWindowTitle(QCoreApplication.translate("Admin_view", u"Form", None))
        self.label_status.setText(QCoreApplication.translate("Admin_view", u"Status", None))
        self.pushButton_edit_user.setText(QCoreApplication.translate("Admin_view", u"Edit", None))
        self.label_selected_province.setText(QCoreApplication.translate("Admin_view", u"Province", None))
        self.label_selected_age.setText(QCoreApplication.translate("Admin_view", u"Age", None))
        self.label_selected_nationality.setText(QCoreApplication.translate("Admin_view", u"Nationality", None))
        self.label_selected_tel.setText(QCoreApplication.translate("Admin_view", u"Tel", None))
        self.label_selected_name.setText(QCoreApplication.translate("Admin_view", u"Name", None))
        self.label_selected_email.setText(QCoreApplication.translate("Admin_view", u"Email", None))
        self.label_selected_id.setText(QCoreApplication.translate("Admin_view", u"ID", None))
        self.label.setText("")
    # retranslateUi

