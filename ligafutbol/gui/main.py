# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: url(:/images/asserts/pattern.png) repeat;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openCamera = QtWidgets.QPushButton(self.centralwidget)
        self.openCamera.setGeometry(QtCore.QRect(30, 20, 88, 27))
        self.openCamera.setObjectName("openCamera")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 791, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuGesti_n = QtWidgets.QMenu(self.menubar)
        self.menuGesti_n.setObjectName("menuGesti_n")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.action_clubs_list = QtWidgets.QAction(MainWindow)
        self.action_clubs_list.setObjectName("action_clubs_list")
        self.action_players_list = QtWidgets.QAction(MainWindow)
        self.action_players_list.setObjectName("action_players_list")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuGesti_n.addAction(self.action_clubs_list)
        self.menuGesti_n.addAction(self.action_players_list)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuGesti_n.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Liga Sanrafaelina de Fútbol"))
        self.openCamera.setText(_translate("MainWindow", "Camara"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuGesti_n.setTitle(_translate("MainWindow", "Gestión"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setStatusTip(_translate("MainWindow", "Salir de la aplicación"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_clubs_list.setText(_translate("MainWindow", "Clubes"))
        self.action_players_list.setText(_translate("MainWindow", "Jugadores"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de..."))

import resources_rc
