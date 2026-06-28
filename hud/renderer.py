import cv2
import time

from hud.colors import PRIMARY


class HUDRenderer:

    def render(self, frame, fps):

        self.draw_title(frame)

        self.draw_status(frame)

        self.draw_fps(frame, fps)

        self.draw_clock(frame)

    def draw_title(self, frame):

        cv2.putText(
            frame,
            "ATLAS",
            (20, 40),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            PRIMARY,
            2,
        )

        cv2.putText(
            frame,
            "Vision Engine",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            PRIMARY,
            1,
        )

    def draw_status(self, frame):

        cv2.putText(
            frame,
            "STATUS : ONLINE",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            PRIMARY,
            2,
        )

    def draw_fps(self, frame, fps):

        cv2.putText(
            frame,
            f"FPS : {int(fps)}",
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            PRIMARY,
            2,
        )

    def draw_clock(self, frame):

        now = time.strftime("%I:%M:%S %p")

        cv2.putText(
            frame,
            now,
            (20, 175),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            PRIMARY,
            2,
        )