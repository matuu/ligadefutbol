from datetime import datetime

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QDesktopServices, QImage, QPixmap

from ligafutbol import VERSION
from ligafutbol.gui.about import Ui_about_dialog
from ligafutbol.utils import LSFDialog


class AboutDialog(LSFDialog, Ui_about_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        mava_logo = QImage(":/images/asserts/mava.png")
        mava_logo = mava_logo.scaled(150, 42, Qt.KeepAspectRatioByExpanding,
                                     Qt.SmoothTransformation)
        self.lbl_logo_brand.setPixmap(QPixmap.fromImage(mava_logo))
        self.lbl_year.setText("© {}".format(datetime.now().year))
        self.lbl_brand.linkActivated.connect(self.open_link)
        self.lbl_version.setText("Versión: {}".format(VERSION))
        self.setFixedSize(self.size())

    def open_link(self, linkStr):
        QDesktopServices.openUrl(QUrl("https://www.mava.com.ar"))
