from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from sqlalchemy import func

from ligafutbol.gui.club_edit import Ui_club_edit
from ligafutbol.gui.clubs_list import Ui_dialog_clubs
from ligafutbol.models import DBSession, Club
from ligafutbol.utils import LSFDialog


class ClubTableModel(QAbstractTableModel):
    """
    Table model for Club objects.
    """
    fields = [
        ("NÚMERO", "numero"),
        ("NOMBRE", "nombre"),
    ]

    def __init__(self, session, model, parent=None):
        super().__init__(parent)
        self.db = session
        self.query = session.query(model)
        self.clubs = None
        self.count = None
        self.filter = None

        self.refresh()

    def refresh(self):

        self.layoutAboutToBeChanged.emit()
        q = self.query
        if self.filter is not None:
            q = q.filter(self.filter)
        q = q.order_by(Club.numero)
        self.clubs = q.all()
        self.count = q.count()
        self.layoutChanged.emit()
        # Send signal to update table
        self.modelReset.emit()

    def set_filter(self, f):
        self.filter = f
        self.refresh()

    def rowCount(self, parent=None, *args, **kwargs):
        return self.count

    def headerData(self, p_int, Qt_Orientation, role=None):
        if Qt_Orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.fields[p_int][0])
        return QVariant()

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.fields)

    def data(self, QModelIndex, role=None):
        if not QModelIndex.isValid():
            return QVariant()

        elif role != Qt.DisplayRole:
            return QVariant()

        clubs = self.clubs[QModelIndex.row()]
        name = self.fields[QModelIndex.column()][1]
        val = getattr(clubs, name)
        return str(val) if val is not None else ''


class ClubListView(LSFDialog, Ui_dialog_clubs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DBSession()
        self.model = ClubTableModel(self.db, Club, self)
        self.table_list_clubes.setModel(self.model)
        self.table_list_clubes.horizontalHeader().setStretchLastSection(True)
        self.table_list_clubes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setFixedSize(self.size())
        # connect signals
        self.btn_close_club.clicked.connect(self.close)
        self.btn_search_clubes.clicked.connect(self.search_clubs)
        self.line_search_clubes.returnPressed.connect(self.search_clubs)
        self.btn_new_club.clicked.connect(self.open_new_club)
        self.btn_edit_club.clicked.connect(self.open_edit_club)
        self.btn_delete_club.clicked.connect(self.delete_club)

    def search_clubs(self):
        txt = self.line_search_clubes.text().strip()
        if txt:
            self.model.set_filter(Club.nombre.like("%{}%".format(txt)))
        else:
            self.model.set_filter(None)

    def refresh(self):
        self.model.refresh()

    def open_new_club(self):
        new_club_dialog = ClubEditView(session=self.db)
        new_club_dialog.exec_()
        self.refresh()

    def open_edit_club(self):
        club = self.get_selected_club()
        if club:
            club_dialog = ClubEditView(session=self.db, club=club)
            club_dialog.exec_()
            self.refresh()

    def delete_club(self):
        club = self.get_selected_club()
        if club:
            ret = QMessageBox.question(
                self, '¿Eliminar club?', "¿Seguro que desea eliminar el club {} (NUM: {})? Esta acción "
                                         "no puede revertirse.".format(club.nombre, club.numero),
                QMessageBox.Yes, QMessageBox.No)

            if ret == QMessageBox.Yes:
                self.db.delete(club)
                self.db.commit()
                self.refresh()
                QMessageBox.information(
                    self, "Club eliminado", "El club {} (NUM: {}) fue eliminado correctamente.".format(
                        club.nombre, club.numero))

    def get_selected_club(self):
        idx = self.table_list_clubes.selectionModel().selectedRows()
        if idx:
            idx = idx[0]
            club = self.model.clubs[idx.row()]
            return club
        return None


class ClubEditView(LSFDialog, Ui_club_edit):
    def __init__(self, session, club=None):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.db = session
        self.save_picture = False
        if club:
            self.is_new = False
            self.club = club
        else:
            self.is_new = True
            self.club = Club()
            try:
                self.club.numero = int(self.db.query(func.max(Club.numero).label('last_num')).one().last_num) + 1
            except TypeError:
                self.club.numero = 1

        self.set_club_to_view()

        self.btn_save.clicked.connect(self.save_club)
        self.btn_cancel.clicked.connect(self.cancel)

    def save_club(self):
        self.get_club_from_view()
        errors = self.club.verify()
        if not errors:
            if (
                (self.is_new and self.db.query(Club).filter(Club.numero == self.club.numero).count()) or
                (not self.is_new and self.db.query(Club).filter(
                       Club.numero == self.club.numero, Club.id != self.club.id).count())):
                QMessageBox.critical(
                    self, "Número de club utilizado", "Existe otro club utilizando el número: {}. "
                                                      "Por favor, utilice otro.".format(self.club.numero))
            else:
                self.db.add(self.club)
                self.db.commit()
                if self.is_new:
                    QMessageBox.information(
                        self, "Club almacenado", "El club {} (NUM: {}) fue guardado con éxito.".format(
                            self.club.nombre, self.club.numero))
                else:
                    QMessageBox.information(
                        self, "Club actualizado", "El club {} (NUM: {}) fue actualizado correctamente.".format(
                            self.club.nombre, self.club.numero))
                self.close()
        else:
            error_msg = "\n".join(errors)
            QMessageBox.critical(self, "Error de validación",
                                 "Ocurrieron algunos errores:\n{}".format(error_msg), QMessageBox.Ok)

    def cancel(self):
        ret = QMessageBox.question(self, '¿Cerrar?', "¿Seguro que desea salir? Perderá los cambios no guardados.",
                                   QMessageBox.Yes, QMessageBox.No)

        if ret == QMessageBox.Yes:
            self.db.rollback()
            self.close()

    def set_club_to_view(self):
        self.line_nombre.setText(self.club.nombre)
        if self.club.numero:
            self.spin_numero.setValue(self.club.numero)

    def get_club_from_view(self):
        self.club.nombre = self.line_nombre.text().strip()
        self.club.numero = int(self.spin_numero.value())
