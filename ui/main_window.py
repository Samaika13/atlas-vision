from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QStackedLayout,
)

from ui.camera_widget import CameraWidget
from hud.overlay import HUDOverlay
from ui.theme import APP_STYLE


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("ATLAS")

        self.resize(1000, 700)

        self.setMinimumSize(900, 600)

        self.setStyleSheet(APP_STYLE)

        root = QWidget()
        self.setCentralWidget(root)

        layout = QStackedLayout()
        layout.setStackingMode(QStackedLayout.StackAll)

        root.setLayout(layout)

        self.camera = CameraWidget()

        self.overlay = HUDOverlay()
        self.overlay.raise_()

        layout.addWidget(self.camera)
        layout.addWidget(self.overlay)

        self.overlay.setGeometry(self.rect())

        self.camera.fps_callback = self.overlay.set_data

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.overlay.setGeometry(self.rect())