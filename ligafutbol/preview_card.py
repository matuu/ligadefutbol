import os
from datetime import datetime

from PyQt5.QtCore import QSizeF
from PyQt5.QtGui import QPageSize
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebEngineWidgets import QWebEngineView

from ligafutbol.gui.preview_card import Ui_dialog_preview_card
from ligafutbol.utils import LSFDialog, render_template


class PreviewCardDialog(LSFDialog, Ui_dialog_preview_card):
    def __init__(self, player, db):
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.db = db

        self.render_card = QWebEngineView()
        self.render_card.setFixedHeight(366)
        self.render_card.setFixedWidth(975)
        # self.setFixedSize(self.size())
        with open(os.path.join(os.path.abspath("."), "asserts", "template.html")) as t:
            template = t.read()

        html_ready_to_render = render_template(template, self.player.dict_to_render())
        self.doc = QTextDocument()
        self.doc.setHtml(html_ready_to_render)
        self.render_card.setHtml(html_ready_to_render)
        self.verticalLayout.addWidget(self.render_card)

        self.btn_close.clicked.connect(self.close)
        self.btn_print.clicked.connect(self.print_player_card)

    def print_player_card(self):
        # este forma de imprimir el pdf, se distorcionó, por agrandar mucho la letra.
        # revisar si luego se utiliza este método
        # page_layout = QPageLayout(QPageSize(QSizeF(210, 90), QPageSize.Millimeter),
        #                           QPageLayout.Portrait, QMarginsF(5, 5, 5, 5))
        # path_pdf = os.path.join(os.path.abspath('.'), 'tmp', 'player_card.pdf')
        # self.render_card.page().printToPdf(path_pdf, page_layout)

        self.printer = QPrinter()
        self.printer.setPageMargins(5, 5, 5, 5, QPrinter.Millimeter)
        self.printer.setPageSize(QPageSize(QSizeF(210, 90), QPageSize.Millimeter))
        self.printer.setOutputFileName('tmp/player_card.pdf')
        self.printer.setResolution(300)

        painter = QPainter(self.printer)
        painter.begin(self.printer)
        xscale = self.printer.pageRect().width() / float(self.render_card.width())
        yscale = self.printer.pageRect().height() / float(self.render_card.height())

        scale = min(xscale, yscale)
        painter.translate(0, 0)
        painter.scale(scale, scale)
        self.render_card.render(painter)
        painter.end()

        self.player.fecha_impresion = datetime.today()
        self.db.add(self.player)
        self.db.commit()
        """
        from sys import platform as _platform

        if _platform.startswith("linux"):
            import subprocess
            lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
            with open(path_pdf, 'rb') as f:
                lpr.stdin.write(f.read())
        elif _platform == "darwin":
            print("No Mac support")
            return
        elif _platform == "win32":
            # Windows
            import win32api
            win32api.ShellExecute(0, "print", path_pdf, None, ".", 0)
        """