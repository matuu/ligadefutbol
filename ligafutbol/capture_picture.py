from PyQt5.QtCore import QRect, QTimer
from PyQt5.QtGui import QPainter, QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from pygame import camera, image as py_image

from ligafutbol.gui import capture_webcam_ui


class CaptureWebcam(QDialog, capture_webcam_ui.Ui_dialog_capture_image):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_cancel_capture.clicked.connect(self.cancel_action)
        self.btn_take_capture.clicked.connect(self.capture_image)
        self.btn_save_capture.clicked.connect(self.save_capture)
        self.setup_camera()
        self.pic_capture = None
        self.cancel = True

    def setup_camera(self):
        """Initialize camera.
        """
        camera.init()
        self.cam = camera.Camera(camera.list_cameras()[0])
        self.cam.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)
        self.overlay = QImage(":/images/asserts/overlay.png")

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        self.pic_capture = self.cam.get_image()
        img_str = py_image.tostring(self.pic_capture, 'RGBA')
        self.last_pic = QImage(img_str, self.pic_capture.get_width(), self.pic_capture.get_height(),
                               QImage.Format_RGBA8888_Premultiplied)
        painter = QPainter()
        painter.begin(self.last_pic)
        painter.drawImage(0, 0, self.overlay)
        painter.end()
        self.img_capture.setPixmap(QPixmap.fromImage(self.last_pic))

    def capture_image(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn_take_capture.setText("Descartar")

        else:
            self.timer.start()
            self.btn_take_capture.setText("Capturar")

    def save_capture(self):
        self.cancel = False
        if self.pic_capture:
            min_side = min(self.pic_capture.get_width(), self.pic_capture.get_height())
            rect = QRect(
                (self.pic_capture.get_width() - min_side) / 2,  # left
                (self.pic_capture.get_height() - min_side) / 2,  # top
                min_side, min_side  # width and height
            )
            self.capture = self.last_pic.copy(rect)
            self.safe_close()

    def safe_close(self):
        self.cam.stop()
        camera.quit()
        self.close()

    def cancel_action(self):
        self.cancel = True
        self.safe_close()
