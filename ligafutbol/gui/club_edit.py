# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/club_edit.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_club_edit(object):
    def setupUi(self, club_edit):
        club_edit.setObjectName("club_edit")
        club_edit.resize(359, 182)
        club_edit.setStyleSheet("background-color: rgb(120, 130, 140);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(club_edit)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 341, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_save.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.widget = QtWidgets.QWidget(club_edit)
        self.widget.setGeometry(QtCore.QRect(10, 10, 341, 111))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.line_nombre = QtWidgets.QLineEdit(self.widget)
        self.line_nombre.setObjectName("line_nombre")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_nombre)
        self.spin_numero = QtWidgets.QSpinBox(self.widget)
        self.spin_numero.setObjectName("spin_numero")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_numero)

        self.retranslateUi(club_edit)
        QtCore.QMetaObject.connectSlotsByName(club_edit)
        club_edit.setTabOrder(self.line_nombre, self.btn_save)
        club_edit.setTabOrder(self.btn_save, self.btn_cancel)

    def retranslateUi(self, club_edit):
        _translate = QtCore.QCoreApplication.translate
        club_edit.setWindowTitle(_translate("club_edit", "Datos del jugador"))
        self.btn_save.setText(_translate("club_edit", "Guardar"))
        self.btn_cancel.setText(_translate("club_edit", "Cancelar"))
        self.label_2.setText(_translate("club_edit", "Número:"))
        self.label_3.setText(_translate("club_edit", "Nombre:"))

import resources_rc
