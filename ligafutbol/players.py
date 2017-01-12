import os
import uuid
from datetime import datetime

from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from sqlalchemy import or_, and_, desc

from ligafutbol.capture_picture import CaptureWebcam
from ligafutbol.gui.player_edit import Ui_player_edit
from ligafutbol.gui.players_list import Ui_dialog_players
from ligafutbol.models import DBSession, Jugador, Club
from ligafutbol.preview_card import PreviewCardDialog
from ligafutbol.utils import slugify, LSFDialog


class PlayerTableModel(QAbstractTableModel):
    """
    Table model for Player objects.
    """
    fields = [
        ("NOMBRE", "nombre"),
        ("APELLIDO", "apellido"),
        ("NACIMIENTO", "fecha_nac"),
        ("CLUB", "club")
    ]

    def __init__(self, session, model, parent=None):
        super().__init__(parent)
        self.db = session
        self.query = session.query(model)
        self.players = None
        self.count = None
        self.filter = None

        self.refresh()

    def refresh(self):

        self.layoutAboutToBeChanged.emit()
        q = self.query
        if self.filter is not None:
            q = q.filter(self.filter)
        q = q.order_by(desc(Jugador.fecha_renovacion))
        if self.filter is None:
            q = q.limit(30)
        self.players = q.all()
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

        player = self.players[QModelIndex.row()]
        name = self.fields[QModelIndex.column()][1]
        val = getattr(player, name)
        if isinstance(val, datetime):
            return val.strftime("%d/%m/%Y")
        elif isinstance(val, Club):
            return val.nombre
        else:
            return str(val) if val is not None else ''


class PlayerListView(LSFDialog, Ui_dialog_players):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DBSession()
        self.model = PlayerTableModel(self.db, Jugador, self)
        self.table_list_players.setModel(self.model)
        self.table_list_players.horizontalHeader().setStretchLastSection(True)
        self.table_list_players.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        selModel = self.table_list_players.selectionModel()
        selModel.selectionChanged.connect(self.show_photo_player)
        self.setFixedSize(self.size())
        # connect signals
        self.btn_close_players.clicked.connect(self.close)
        self.btn_search_players.clicked.connect(self.search_players)
        self.line_search_players.returnPressed.connect(self.search_players)
        self.btn_new_player.clicked.connect(self.open_new_player)
        self.btn_edit_player.clicked.connect(self.open_edit_player)
        self.btn_delete_player.clicked.connect(self.delete_player)
        self.btn_print_player_card.clicked.connect(self.show_preview_card)

    def search_players(self):
        txt = self.line_search_players.text().strip()
        if txt:
            expression = []
            for term in txt.split(' '):
                expression.append(
                    or_(Jugador.nombre.like("%{}%".format(term)), Jugador.apellido.like("{}%".format(term))))
            self.model.set_filter(and_(*[exp for exp in expression]))
        else:
            self.model.set_filter(None)

    def refresh(self):
        self.model.refresh()
        self.table_list_players.selectRow(0)
        self.show_photo_player()

    def show_photo_player(self):
        player = self.get_selected_player()
        if player:
            img_path = player.avatar
            if not os.path.exists(img_path):
                img_path = Jugador.get_default_avatar()
        else:
            img_path = Jugador.get_default_avatar()
        img = QPixmap(img_path)
        self.lbl_photo_player.setPixmap(img.scaled(
            self.lbl_photo_player.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def open_new_player(self):
        new_player_dialog = PlayerEditView(session=self.db)
        new_player_dialog.exec_()
        self.refresh()

    def open_edit_player(self):
        player = self.get_selected_player()
        if player:
            new_player_dialog = PlayerEditView(session=self.db, player=player)
            new_player_dialog.exec_()
            self.refresh()

    def delete_player(self):
        player = self.get_selected_player()
        if player:
            ret = QMessageBox.question(self, '¿Eliminar jugador?',
                                       "¿Seguro que desea eliminar el jugador {} {}? Esta acción no "
                                       "puede revertirse.".format(player.nombre, player.apellido),
                                       QMessageBox.Yes, QMessageBox.No)

            if ret == QMessageBox.Yes:
                self.db.delete(player)
                self.db.commit()
                self.refresh()
                QMessageBox.information(
                    self, "Jugador eliminado", "El jugador {} {} fue eliminado correctamente.".format(
                        player.nombre, player.apellido))

    def show_preview_card(self):
        player = self.get_selected_player()
        if player:
            preview_card = PreviewCardDialog(player, self.db)
            preview_card.exec_()

    def get_selected_player(self):
        idx = self.table_list_players.selectionModel().selectedRows()
        if idx:
            idx = idx[0]
            player = self.model.players[idx.row()]
            return player
        return None


class PlayerEditView(LSFDialog, Ui_player_edit):
    def __init__(self, session, player=None):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.db = session
        self.save_picture = False
        if player:
            self.is_new = False
            self.player = player
        else:
            self.is_new = True
            self.btn_print_card.setEnabled(False)
            self.player = Jugador()
            self.player.fecha_inscripcion = datetime.now()
        self.load_clubes_combo()
        self.set_player_to_view()

        self.btn_save.clicked.connect(self.save_player)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_change_photo.clicked.connect(self.open_camera)
        self.btn_print_card.clicked.connect(self.show_preview_card)

    def load_clubes_combo(self):
        clubes = self.db.query(Club).all()
        self.cmb_clubes.clear()
        for club in clubes:
            self.cmb_clubes.addItem(club.nombre, club.id)

    def open_camera(self):
        dialog_capture_image = CaptureWebcam()
        dialog_capture_image.exec_()
        if not dialog_capture_image.cancel:
            self.save_picture = True
            self.taken_picture = dialog_capture_image.capture  # QImage
            self.lbl_photo_player.setPixmap(QPixmap.fromImage(dialog_capture_image.capture))

    def show_preview_card(self):
        if not self.is_new:
            preview_card = PreviewCardDialog(self.player, self.db)
            preview_card.exec_()

    def save_player(self):
        self.get_player_from_view()
        errors = self.player.verify()
        if not errors:
            # save picture
            if self.save_picture:
                name = "{}_{}_{}.jpg".format(slugify(self.player.nombre), slugify(self.player.apellido), uuid.uuid4())
                self.player.foto = name
                self.taken_picture.save(self.player.avatar, 'jpg', 90)
            if not self.is_new:
                self.player.fecha_renovacion = datetime.now()
            self.db.add(self.player)
            self.db.commit()
            if self.is_new:
                QMessageBox.information(
                    self, "Jugador almacenado", "El jugador {} {} fue guardado con éxito.".format(
                        self.player.nombre, self.player.apellido))
            else:
                QMessageBox.information(
                    self, "Jugador actualizado", "El jugador {} {} fue actualizado correctamente.".format(
                        self.player.nombre, self.player.apellido))
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

    def set_player_to_view(self):
        self.line_nombre.setText(self.player.nombre)
        self.line_apellido.setText(self.player.apellido)
        if self.player.fecha_nac:
            self.date_fecha_nac.setDate(self.player.fecha_nac)
        self.line_lugar_nac.setText(self.player.lugar_nac)
        self.line_provincia.setText(self.player.provincia)
        self.line_dni.setText(str(self.player.dni or 0))
        self.line_domicilio.setText(self.player.domicilio)
        if self.player.fecha_inscripcion:
            self.date_fecha_incripcion.setDate(self.player.fecha_inscripcion)
        if not self.is_new:
            self.date_fecha_incripcion.setEnabled(False)
        self.pin_division.setValue(self.player.division or 0)
        self.txt_observaciones.setText(self.player.observaciones)
        if self.player.fecha_renovacion:
            self.lbl_fecha_renovacion.setText(self.player.fecha_renovacion.strftime("%d/%m/%Y %H1:%M"))
        self.lbl_fecha_vigencia.setText(self.player.vigencia.strftime("%d/%m/%Y") if self.player.vigencia else '')
        # avatar
        if os.path.exists(self.player.avatar):
            img = QPixmap(self.player.avatar)
        else:
            img = QPixmap(Jugador.get_default_avatar())
        self.lbl_photo_player.setPixmap(img.scaled(
            self.lbl_photo_player.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        if self.player.club_id:
            self.cmb_clubes.setCurrentIndex(self.cmb_clubes.findData(self.player.club_id))

    def get_player_from_view(self):
        self.player.nombre = self.line_nombre.text().strip()
        self.player.apellido = self.line_apellido.text().strip()
        self.player.fecha_nac = self.date_fecha_nac.date().toPyDate() or None
        self.player.lugar_nac = self.line_lugar_nac.text().strip()
        self.player.provincia = self.line_provincia.text().strip()
        self.player.dni = self.line_dni.text()
        self.player.domicilio = self.line_domicilio.text().strip()
        self.player.fecha_inscripcion = self.date_fecha_incripcion.date().toPyDate() or None
        self.player.division = self.pin_division.value()
        self.player.observaciones = self.txt_observaciones.toPlainText()
        if self.cmb_clubes.currentIndex():
            self.player.club_id = self.cmb_clubes.itemData(self.cmb_clubes.currentIndex())
