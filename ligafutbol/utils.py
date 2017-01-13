import random
import string
from datetime import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog


def slugify(txt):
    txt = str(txt)
    return txt.upper().strip().replace(' ', '_')


def random_string():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))


def render_template(svg, dict):
    for var in dict.keys():
        svg = svg.replace("[{}]".format(var), str(dict[var]))
    return svg


class LSFDialog(QDialog):
    """
    Un dialogo con icono definido
    """
    def __init__(self, **args):
        super().__init__(**args)
        self.setWindowIcon(QIcon(":/images/asserts/logo-lsf.svg"))
