import time

from hud.panel import HUDPanel
from hud.widgets import LabelWidget


class HUDRenderer:

    def __init__(self):

        self.panel = HUDPanel()
        self.widget = LabelWidget()

    def render(self, frame, fps):

        self.panel.draw(frame)

        self.draw_title(frame)

        self.draw_status(frame)

        self.draw_fps(frame, fps)

        self.draw_camera(frame)

        self.draw_clock(frame)

    def draw_title(self, frame):

        self.widget.draw(
            frame,
            "ATLAS",
            "Vision Engine",
            30,
            45
        )

    def draw_status(self, frame):

        self.widget.draw(
            frame,
            "STATUS",
            "ONLINE",
            30,
            85
        )

    def draw_fps(self, frame, fps):

        self.widget.draw(
            frame,
            "FPS",
            str(int(fps)),
            30,
            125
        )

    def draw_camera(self, frame):

        self.widget.draw(
            frame,
            "CAMERA",
            "CONNECTED",
            30,
            165
        )

    def draw_clock(self, frame):

        current = time.strftime("%I:%M:%S %p")

        self.widget.draw(
            frame,
            "TIME",
            current,
            30,
            205
        )