from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtWidgets import QLabel
from sqlalchemy import func

from ligafutbol.about import AboutDialog
from ligafutbol.clubs import ClubListView
from ligafutbol.gui.main import Ui_MainWindow
from ligafutbol.models import DBSession, Jugador
from ligafutbol.players import PlayerListView
from ligafutbol import VERSION


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

    def resizeEvent(self, resizeEvent):
        self.load_background()

    def load_background(self):
        oImage = QImage(':/images/asserts/fondo_liga.png')
        sImage = oImage.scaled(self.size(), Qt.KeepAspectRatioByExpanding,
                               Qt.SmoothTransformation)  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(sImage))
        self.setPalette(palette)


class LigaDeFutbolApp(Ui_MainWindow):

    def __init__(self, main):
        super().__init__()
        self.main_window = main
        self.setupUi(main)
        self.init_ui()

    def init_ui(self):
        lbl_version = QLabel()
        lbl_version.setText("Versión: {}".format(VERSION))
        self.statusbar.addWidget(lbl_version)

        self.main_window.load_background()
        self.main_window.center()
        self.actionSalir.triggered.connect(self.main_window.close)
        self.action_players_list.triggered.connect(self.show_players_list)
        self.action_clubs_list.triggered.connect(self.show_clubs_list)
        self.actionAcerca_de.triggered.connect(self.show_about_dialog)

    def show_players_list(self):
        player_list = PlayerListView()
        player_list.exec_()

    def show_clubs_list(self):
        club_list = ClubListView()
        club_list.exec_()

    def show_about_dialog(self):
        about = AboutDialog()
        about.exec_()

    def get_player_card_today(self):
        db = DBSession()
        players = db.query(Jugador).filter(func.date(Jugador.fecha_impresion) == datetime.today()).all()
        print(players)
