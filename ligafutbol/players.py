from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget

from ligafutbol.gui.jugadores_list import Ui_Form as player_list_view


class PlayerListView(QDialog, player_list_view):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
