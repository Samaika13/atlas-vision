import cv2
import time

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel

from core.config import CAMERA_INDEX, MIRROR_CAMERA

from hud.renderer import HUDRenderer
from vision.face_detector import FaceDetector

from audio.system_state import STATE


class CameraWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.prev = time.time()

        self.hud = HUDRenderer()

        self.detector = FaceDetector()

    def update_frame(self):

        success, frame = self.cap.read()

        if not success:
            return

        if MIRROR_CAMERA:
            frame = cv2.flip(frame, 1)

        current = time.time()

        fps = 1 / max(current - self.prev, 0.0001)
        STATE.set_fps(fps)

        self.prev = current

        faces = self.detector.detect(frame)
        STATE.set_faces(len(faces))

        frame = self.hud.draw(
            frame,
            STATE,
            faces
        )

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb.shape

        image = QImage(
            rgb.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(image)

        pixmap = pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(pixmap)

    def closeEvent(self, event):

        self.cap.release()

        event.accept()