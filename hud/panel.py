import cv2

from hud.colors import PRIMARY


class HUDPanel:

    def draw(self, frame):

        overlay = frame.copy()

        x = 10
        y = 10
        w = 300
        h = 220

        cv2.rectangle(
            overlay,
            (x, y),
            (x + w, y + h),
            (20, 20, 20),
            -1
        )

        alpha = 0.35

        cv2.addWeighted(
            overlay,
            alpha,
            frame,
            1 - alpha,
            0,
            frame
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            PRIMARY,
            2
        )