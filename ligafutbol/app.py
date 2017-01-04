#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtWidgets import QMdiSubWindow

from ligafutbol.gui.main import Ui_MainWindow
from ligafutbol.capture_picture import CaptureWebcam
from ligafutbol.players import PlayerListView


class LSFMainWindow(QMainWindow):
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Salir', "¿Seguro que desea salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """
        Centrar en la pantalla.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class LigaDeFutbolApp(Ui_MainWindow):

    def __init__(self, main):
        super().__init__()
        self.main_window = main
        self.setupUi(main)
        self.init_ui()

    def init_ui(self):
        self.main_window.center()
        self.actionSalir.triggered.connect(self.main_window.close)
        self.action_players_list.triggered.connect(self.show_players_list)
        self.openCamera.clicked.connect(self.open_camera)

    def open_camera(self):
        dialog_capture_image = CaptureWebcam()
        dialog_capture_image.exec_()
        print(dialog_capture_image.cancel)

    def show_players_list(self):
        print("show")
        player_list = PlayerListView()
        player_list.exec_()

###################
#  Event handler  #
###################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = LSFMainWindow()
    liga_app = LigaDeFutbolApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
