import random
import string

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox


def slugify(txt):
    txt = str(txt)
    return txt.upper().strip().replace(' ', '_')


def random_string():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))


def render_template(svg, dict):
    for var in dict.keys():
        svg = svg.replace("[{}]".format(var), str(dict[var]))
    return svg


def pregunta_sino(title, message):
    box = QMessageBox()
    box.setIcon(QMessageBox.Question)
    box.setWindowTitle(title)
    box.setText(message)
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = box.button(QMessageBox.Yes)
    buttonY.setText('Si')
    buttonN = box.button(QMessageBox.No)
    buttonN.setText('No')
    result = box.exec_()
    return result


class LSFDialog(QDialog):
    """
    Un dialogo con icono definido
    """
    def __init__(self, **args):
        super().__init__(**args)
        self.setWindowIcon(QIcon(":/images/asserts/logo-lsf.svg"))
