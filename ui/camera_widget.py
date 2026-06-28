import time
import cv2

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel

from core.config import CAMERA_INDEX, MIRROR_CAMERA


class CameraWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.")

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_frame)

        self.timer.start(30)  # ~33 FPS

        self.prev = time.time()

        self.fps_callback = None

    def update_frame(self):

        success, frame = self.cap.read()

        if not success:
            return

        if MIRROR_CAMERA:
            frame = cv2.flip(frame, 1)

        # ---------- FPS ----------

        current = time.time()

        fps = 1 / max(current - self.prev, 0.0001)

        self.prev = current

        if self.fps_callback:
            self.fps_callback(fps, 0)

        # ---------- Convert to Qt ----------

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb.shape

        image = QImage(
            rgb.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888,
        )

        pixmap = QPixmap.fromImage(image)

        pixmap = pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        self.setPixmap(pixmap)

    def closeEvent(self, event):

        if self.cap.isOpened():
            self.cap.release()

        super().closeEvent(event)