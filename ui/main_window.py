from PySide6.QtWidgets import (
    QMainWindow,
)

from ui.camera_widget import CameraWidget
from ui.theme import APP_STYLE

from audio.microphone import Microphone

from PySide6.QtGui import QShortcut, QKeySequence


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("ATLAS")

        self.resize(1000, 700)

        self.setMinimumSize(900, 600)

        self.setStyleSheet(APP_STYLE)

        self.camera = CameraWidget()

        self.microphone = Microphone()
        self.microphone.start()

        self.shortcut = QShortcut(
            QKeySequence("Ctrl+A"),
            self
        )

        self.shortcut.activated.connect(
            self.microphone.activate
        )

        self.setCentralWidget(self.camera)