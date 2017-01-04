import sys
from pygame import camera, image as py_image

from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QWidget

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

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        self.pic_capture = self.cam.get_image()
        img_str = py_image.tostring(self.pic_capture, 'RGBA')
        image = QImage(img_str, self.pic_capture.get_width(), self.pic_capture.get_height(),
                       QImage.Format_RGBA8888_Premultiplied)
        self.img_capture.setPixmap(QPixmap.fromImage(image))

    def capture_image(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn_take_capture.setText("Descartar")

        else:
            self.timer.start()
            self.btn_take_capture.setText("Capturar")

    def save_capture(self):
        self.cancel = False
        if self.img_capture:
            py_image.save(self.pic_capture, "tmp/photo.jpg")
            self.safe_close()

    def safe_close(self):
        self.cam.stop()
        camera.quit()
        self.close()

    def cancel_action(self):
        self.cancel = True
        self.safe_close()