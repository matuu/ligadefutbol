# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/clubs_list.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_clubs(object):
    def setupUi(self, dialog_clubs):
        dialog_clubs.setObjectName("dialog_clubs")
        dialog_clubs.resize(439, 486)
        dialog_clubs.setStyleSheet("background-color: rgb(120, 130, 140);")
        dialog_clubs.setModal(True)
        self.gridLayoutWidget = QtWidgets.QWidget(dialog_clubs)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 421, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.line_search_clubes = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_search_clubes.setObjectName("line_search_clubes")
        self.gridLayout.addWidget(self.line_search_clubes, 0, 1, 1, 1)
        self.btn_search_clubes = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_search_clubes.setAutoFillBackground(False)
        self.btn_search_clubes.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_search_clubes.setDefault(False)
        self.btn_search_clubes.setFlat(False)
        self.btn_search_clubes.setObjectName("btn_search_clubes")
        self.gridLayout.addWidget(self.btn_search_clubes, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_new_club = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_new_club.setAutoFillBackground(False)
        self.btn_new_club.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_new_club.setDefault(False)
        self.btn_new_club.setFlat(False)
        self.btn_new_club.setObjectName("btn_new_club")
        self.verticalLayout.addWidget(self.btn_new_club)
        self.btn_edit_club = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_edit_club.setAutoFillBackground(False)
        self.btn_edit_club.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_edit_club.setFlat(False)
        self.btn_edit_club.setObjectName("btn_edit_club")
        self.verticalLayout.addWidget(self.btn_edit_club)
        self.btn_delete_club = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_delete_club.setAutoFillBackground(False)
        self.btn_delete_club.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_delete_club.setFlat(False)
        self.btn_delete_club.setObjectName("btn_delete_club")
        self.verticalLayout.addWidget(self.btn_delete_club)
        self.btn_close_club = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_close_club.setAutoFillBackground(False)
        self.btn_close_club.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_close_club.setFlat(False)
        self.btn_close_club.setObjectName("btn_close_club")
        self.verticalLayout.addWidget(self.btn_close_club)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.table_list_clubes = QtWidgets.QTableView(self.gridLayoutWidget)
        self.table_list_clubes.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table_list_clubes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_list_clubes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_list_clubes.setObjectName("table_list_clubes")
        self.gridLayout.addWidget(self.table_list_clubes, 1, 1, 1, 1)

        self.retranslateUi(dialog_clubs)
        QtCore.QMetaObject.connectSlotsByName(dialog_clubs)

    def retranslateUi(self, dialog_clubs):
        _translate = QtCore.QCoreApplication.translate
        dialog_clubs.setWindowTitle(_translate("dialog_clubs", "Listado de clubes"))
        self.btn_search_clubes.setText(_translate("dialog_clubs", "Buscar"))
        self.btn_new_club.setText(_translate("dialog_clubs", "Nuevo"))
        self.btn_edit_club.setText(_translate("dialog_clubs", "Editar"))
        self.btn_delete_club.setText(_translate("dialog_clubs", "Eliminar"))
        self.btn_close_club.setText(_translate("dialog_clubs", "Cerrar"))

import resources_rc
