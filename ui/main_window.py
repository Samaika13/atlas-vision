from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from ui.theme import APP_STYLE


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("ATLAS")

        self.resize(1280, 720)

        self.setStyleSheet(APP_STYLE)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        title = QLabel("ATLAS")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:40px;
            font-weight:bold;
            color:#00E5FF;
        """)

        subtitle = QLabel("Vision Engine")

        subtitle.setAlignment(Qt.AlignCenter)

        layout.addStretch()

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addStretch()