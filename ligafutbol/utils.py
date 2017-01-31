import random
import string
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox


home = os.path.expanduser("~")
application_home = os.path.join(home, "LigaFutbol")


def get_application_folder(folder=None, file=None):
    if not folder and file:
        return os.path.join(application_home, file)
    elif folder and not file:
        return os.path.join(application_home, folder)
    elif not folder and not file:
        return application_home
    else:
        return os.path.join(application_home, folder, file)


def get_asserts_dir(file):
    if hasattr(sys, "frozen"):
        main_dir = os.path.dirname(sys.executable)
    else:
        main_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    return os.path.join(main_dir, 'ligafutbol', 'asserts', file)

def exists_or_create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

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
