# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture_webcam_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_capture_image(object):
    def setupUi(self, dialog_capture_image):
        dialog_capture_image.setObjectName("dialog_capture_image")
        dialog_capture_image.setWindowModality(QtCore.Qt.WindowModal)
        dialog_capture_image.resize(661, 536)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_capture_image.sizePolicy().hasHeightForWidth())
        dialog_capture_image.setSizePolicy(sizePolicy)
        dialog_capture_image.setModal(True)
        self.img_capture = QtWidgets.QLabel(dialog_capture_image)
        self.img_capture.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.img_capture.setAutoFillBackground(False)
        self.img_capture.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.img_capture.setText("")
        self.img_capture.setObjectName("img_capture")
        self.horizontalLayoutWidget = QtWidgets.QWidget(dialog_capture_image)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(8, 490, 641, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_take_capture = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_take_capture.sizePolicy().hasHeightForWidth())
        self.btn_take_capture.setSizePolicy(sizePolicy)
        self.btn_take_capture.setObjectName("btn_take_capture")
        self.horizontalLayout.addWidget(self.btn_take_capture)
        self.btn_save_capture = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_capture.sizePolicy().hasHeightForWidth())
        self.btn_save_capture.setSizePolicy(sizePolicy)
        self.btn_save_capture.setObjectName("btn_save_capture")
        self.horizontalLayout.addWidget(self.btn_save_capture)
        self.btn_cancel_capture = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel_capture.sizePolicy().hasHeightForWidth())
        self.btn_cancel_capture.setSizePolicy(sizePolicy)
        self.btn_cancel_capture.setObjectName("btn_cancel_capture")
        self.horizontalLayout.addWidget(self.btn_cancel_capture)

        self.retranslateUi(dialog_capture_image)
        QtCore.QMetaObject.connectSlotsByName(dialog_capture_image)

    def retranslateUi(self, dialog_capture_image):
        _translate = QtCore.QCoreApplication.translate
        dialog_capture_image.setWindowTitle(_translate("dialog_capture_image", "Capture la foto"))
        self.btn_take_capture.setText(_translate("dialog_capture_image", "Capturar"))
        self.btn_save_capture.setText(_translate("dialog_capture_image", "Guardar"))
        self.btn_cancel_capture.setText(_translate("dialog_capture_image", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_capture_image = QtWidgets.QDialog()
    ui = Ui_dialog_capture_image()
    ui.setupUi(dialog_capture_image)
    dialog_capture_image.show()
    sys.exit(app.exec_())

