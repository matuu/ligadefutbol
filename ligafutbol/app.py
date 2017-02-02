import os
import sys
import subprocess
from PyQt5 import QtWidgets
from datetime import datetime

from PyQt5.QtCore import QFile
from PyQt5.QtCore import QTextStream
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget, qApp
from PyQt5.QtWidgets import QLabel
from sqlalchemy import func

from ligafutbol.about import AboutDialog
from ligafutbol.clubs import ClubListView
from ligafutbol.export import ExportarImpresiones
from ligafutbol.gui.main import Ui_MainWindow
from ligafutbol.models import DBSession, Jugador
from ligafutbol.players import PlayerListView
from ligafutbol.utils import pregunta_sino, get_application_folder
from ligafutbol import VERSION


class LSFMainWindow(QMainWindow):
    def closeEvent(self, event):
        reply = pregunta_sino('Salir', "¿Seguro que desea salir?")
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

        self.action_report = QtWidgets.QAction(main)
        self.action_report.setObjectName("action_report")
        self.menuGesti_n.addAction(self.action_report)
        self.action_report.setText("Reporte de impresiones del día")

        self.init_ui()

    def init_ui(self):
        file = QFile(":/styles/style.qss")
        if file.open(QFile.ReadOnly | QFile.Text):
            ts = QTextStream(file)
            stylesheet = ts.readAll()
            qApp.setStyleSheet(stylesheet)

        lbl_version = QLabel()
        lbl_version.setText("Versión: {}".format(VERSION))
        self.statusbar.addWidget(lbl_version)

        self.main_window.load_background()
        self.main_window.center()
        self.actionSalir.triggered.connect(self.main_window.close)
        self.action_players_list.triggered.connect(self.show_players_list)
        self.action_clubs_list.triggered.connect(self.show_clubs_list)
        self.actionAcerca_de.triggered.connect(self.show_about_dialog)
        self.action_report.triggered.connect(self.generar_reporte_impresion)

    def show_players_list(self):
        player_list = PlayerListView()
        player_list.exec_()

    def show_clubs_list(self):
        club_list = ClubListView()
        club_list.exec_()

    def show_about_dialog(self):
        about = AboutDialog()
        about.exec_()

    def generar_reporte_impresion(self):
        db = DBSession()
        hoy = datetime.today().date()
        players = db.query(Jugador).filter(func.date(Jugador.fecha_impresion) == hoy).all()
        if len(players) == 0:
            QMessageBox.warning(None, "Reporte vacio",
                                "No se registran impresiones durante el día de hoy.")
            return
        file_path = get_application_folder(file='impresiones-{}.xlsx'.format(hoy.strftime("%d-%m-%Y")))
        exportar = ExportarImpresiones(file_path)
        report = exportar.generar_xlsx(players)
        if report:
            if sys.platform.startswith('linux'):
                subprocess.call(["xdg-open", file_path])
            else:
                os.startfile(file_path)
            QMessageBox.information(None, "Reporte generado",
                                    "El reporte se encuentra en {}.".format(file_path))
        else:
            QMessageBox.critical(None, "Reporte NO generado",
                                 "Ocurrió un error al generar el reporte. Intente nuevamente")
        """
        Limpiar la db
        In [43]: b40 = datetime(day=31,month=12,year=1976)
        In [43]: viejos = db.query(Jugador).filter(Jugador.fecha_nac <= b40).all()

        In [40]: b35 = datetime(day=31,month=12,year=1981)
        In [41]: viejos2 = db.query(Jugador).filter(Jugador.fecha_nac <= b35).all()


        """