import os
from datetime import datetime

from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QMessageBox

from ligafutbol.gui.preview_card import Ui_dialog_preview_card
from ligafutbol.utils import LSFDialog, render_template, get_application_folder, get_asserts_dir


class PreviewCardDialog(LSFDialog, Ui_dialog_preview_card):
    def __init__(self, parent, player, db):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.player = player
        self.db = db
        # creación del SVG con la información del jugador
        # cargamos un template con el diseño del carnet, y campos especiales. ej: [club]
        # reemplazamos todos los campos especiales con la información e imagen del jugador
        # escribimos un archivo temporal para renderizarlo en la vista, y posteriormente imprimirlo.

        # Tenemos un svg para mostrarlo, y otro para la impresora. Solución para la orientación de la impresora
        template_preview_path = get_asserts_dir("template_preview.svg")
        template_print_path = get_asserts_dir("template_printer.svg")
        tmp_folder = get_application_folder("tmp")
        if not os.path.exists(tmp_folder):
            os.makedirs(tmp_folder)
        tmp_svg_preview_path = os.path.join(tmp_folder, "card_preview.svg")
        tmp_svg_printer_path = os.path.join(tmp_folder, "card_print.svg")
        with open(template_preview_path, 'r')as f:
            template_svg_data = f.read()
        with open(template_print_path, 'r')as f:
            template_svg_data_print = f.read()
        svg_data = render_template(template_svg_data, self.player.dict_to_render())
        svg_print_data = render_template(template_svg_data_print, self.player.dict_to_render())
        tmp_file = open(tmp_svg_preview_path, 'w')
        tmp_file.write(svg_data)
        tmp_file.close()
        tmp_file = open(tmp_svg_printer_path, 'w')
        tmp_file.write(svg_print_data)
        tmp_file.close()

        self.renderer = QSvgRenderer()
        self.renderer.load(tmp_svg_printer_path)
        if not self.renderer.isValid():
            self.btn_print.setEnabled(False)
            return

        # Crear vista previa
        image = QImage(793.7, 340.15, QImage.Format_ARGB32_Premultiplied)
        image.fill(0xaa888888)
        # Renderizamos el svg tempral dentro del QImage
        # Luego este será el pixmap del Qlabel
        renderer_preview = QSvgRenderer()
        renderer_preview.load(tmp_svg_preview_path)
        if renderer_preview.isValid():
            painter = QPainter(image)
            renderer_preview.render(painter)
            painter.end()
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QPixmap.fromImage(image))
        self.label_2.setFixedSize(793.7, 340.15)
        self.setFixedSize(self.size())

        # signals
        self.btn_close.clicked.connect(self.close)
        self.btn_print.clicked.connect(self.print_player_card)

    def print_player_card(self):
        printer = QPrinter()
        printer.setOrientation(QPrinter.Portrait)
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
        printer.setPageSize(QPrinter.Legal)
        # printer.setFullPage(True)
        # printer.setOutputFormat(QPrinter.NativeFormat)
        # printer.setOutputFileName('tmp/player_card.pdf')

        printer.setResolution(300)
        painter = QPainter()
        painter.begin(printer)
        self.renderer.render(painter)
        painter.end()
        QMessageBox.information(self, "Impresión", "Se creó correctamente la tarea de impresión.")
        self.player.fecha_impresion = datetime.today()
        self.db.add(self.player)
        self.db.commit()
        self.close()
