# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/preview_card.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_preview_card(object):
    def setupUi(self, dialog_preview_card):
        dialog_preview_card.setObjectName("dialog_preview_card")
        dialog_preview_card.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog_preview_card.resize(829, 422)
        dialog_preview_card.setStyleSheet("")
        dialog_preview_card.setSizeGripEnabled(True)
        dialog_preview_card.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog_preview_card)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 813, 403))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
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
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(793, 340))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("border-color: rgb(158, 162, 158);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(dialog_preview_card)
        QtCore.QMetaObject.connectSlotsByName(dialog_preview_card)

    def retranslateUi(self, dialog_preview_card):
        _translate = QtCore.QCoreApplication.translate
        dialog_preview_card.setWindowTitle(_translate("dialog_preview_card", "Vista previa - Credencial"))
        self.btn_print.setText(_translate("dialog_preview_card", "Imprimir"))
        self.btn_close.setText(_translate("dialog_preview_card", "Cancelar"))

