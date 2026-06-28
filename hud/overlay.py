from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget

from datetime import datetime


class HUDOverlay(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.fps = 0
        self.face_count = 0
        self.status = "ONLINE"

        self.scan_y = 0

        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer()

        self.timer.timeout.connect(self.animate)

        self.timer.start(16)

        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_AlwaysStackOnTop)

    def animate(self):

        self.scan_y += 3

        if self.scan_y > self.height():

            self.scan_y = 0

        self.update()

    def set_data(self, fps, faces):

        self.fps = fps
        self.face_count = faces

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        self.draw_grid(painter)

        self.draw_scanline(painter)

        self.draw_panel(painter)

    def draw_grid(self, painter):

        pen = QPen(QColor(0, 180, 255, 25))

        painter.setPen(pen)

        spacing = 40

        for x in range(0, self.width(), spacing):

            painter.drawLine(x, 0, x, self.height())

        for y in range(0, self.height(), spacing):

            painter.drawLine(0, y, self.width(), y)

    def draw_scanline(self, painter):

        pen = QPen(QColor(0, 255, 255, 120))

        pen.setWidth(2)

        painter.setPen(pen)

        painter.drawLine(
            0,
            self.scan_y,
            self.width(),
            self.scan_y
        )

    def draw_panel(self, painter):

        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor(15, 20, 30, 180))

        painter.drawRoundedRect(
            20,
            20,
            300,
            220,
            18,
            18
        )

        pen = QPen(QColor(0, 230, 255))

        pen.setWidth(2)

        painter.setPen(pen)

        painter.drawRoundedRect(
            20,
            20,
            300,
            220,
            18,
            18
        )

        painter.setPen(QColor(0, 255, 255))

        title = QFont()

        title.setPointSize(20)

        title.setBold(True)

        painter.setFont(title)

        painter.drawText(
            40,
            55,
            "ATLAS"
        )

        font = QFont()

        font.setPointSize(11)

        painter.setFont(font)

        painter.drawText(
            40,
            95,
            f"STATUS : {self.status}"
        )

        painter.drawText(
            40,
            125,
            f"FPS : {int(self.fps)}"
        )

        painter.drawText(
            40,
            155,
            f"FACES : {self.face_count}"
        )

        current = datetime.now().strftime("%H:%M:%S")

        painter.drawText(
            40,
            185,
            f"TIME : {current}"
        )

        painter.drawText(
            40,
            215,
            "MIC : STANDBY"
        )

    def resizeEvent(self, event):
        self.update()
        super().resizeEvent(event)