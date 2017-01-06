# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/preview_card.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_preview_card(object):
    def setupUi(self, dialog_preview_card):
        dialog_preview_card.setObjectName("dialog_preview_card")
        dialog_preview_card.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog_preview_card.resize(975, 366)
        dialog_preview_card.setStyleSheet("background-color: rgb(120, 130, 140);")
        dialog_preview_card.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog_preview_card)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 971, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_print = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_print.setObjectName("btn_print")
        self.horizontalLayout_2.addWidget(self.btn_print)
        self.btn_close = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialog_preview_card)
        QtCore.QMetaObject.connectSlotsByName(dialog_preview_card)

    def retranslateUi(self, dialog_preview_card):
        _translate = QtCore.QCoreApplication.translate
        dialog_preview_card.setWindowTitle(_translate("dialog_preview_card", "Vista previa - Credencial"))
        self.btn_print.setText(_translate("dialog_preview_card", "Imprimir"))
        self.btn_close.setText(_translate("dialog_preview_card", "Cancelar"))

