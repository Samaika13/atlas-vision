import cv2
import math
from datetime import datetime


class HUDRenderer:

    def __init__(self):
        self.tick = 0

    def draw_target(self, frame, x, y, w, h):

        c = (255, 255, 0)

        L = 25
        T = 3

        # Top Left
        cv2.line(frame, (x, y), (x + L, y), c, T)
        cv2.line(frame, (x, y), (x, y + L), c, T)

        # Top Right
        cv2.line(frame, (x + w, y), (x + w - L, y), c, T)
        cv2.line(frame, (x + w, y), (x + w, y + L), c, T)

        # Bottom Left
        cv2.line(frame, (x, y + h), (x + L, y + h), c, T)
        cv2.line(frame, (x, y + h), (x, y + h - L), c, T)

        # Bottom Right
        cv2.line(frame, (x + w, y + h), (x + w - L, y + h), c, T)
        cv2.line(frame, (x + w, y + h), (x + w, y + h - L), c, T)

    def draw(
        self,
        frame,
        state,
        detections=None
    ):

        self.tick += 1

        if detections is None:
            detections = []

        h, w = frame.shape[:2]

        cyan = (255, 255, 0)
        dark = (18, 18, 28)
        grid = (55, 85, 95)

        spacing = 55

        # Grid
        for x in range(0, w, spacing):
            cv2.line(frame, (x, 0), (x, h), grid, 1)

        for y in range(0, h, spacing):
            cv2.line(frame, (0, y), (w, y), grid, 1)

        # Animated scan line
        scan = (self.tick * 5) % h
        cv2.line(frame, (0, scan), (w, scan), (255, 255, 100), 2)

        # Glass panel
        overlay = frame.copy()

        cv2.rectangle(
            overlay,
            (20, 20),
            (340, 240),
            dark,
            -1
        )

        cv2.addWeighted(
            overlay,
            0.45,
            frame,
            0.55,
            0,
            frame
        )

        # Border
        cv2.rectangle(frame, (20, 20), (340, 240), cyan, 2)

        L = 18
        T = 3

        # Decorative corners
        cv2.line(frame, (20, 20), (20 + L, 20), cyan, T)
        cv2.line(frame, (20, 20), (20, 20 + L), cyan, T)

        cv2.line(frame, (340, 20), (340 - L, 20), cyan, T)
        cv2.line(frame, (340, 20), (340, 20 + L), cyan, T)

        cv2.line(frame, (20, 240), (20 + L, 240), cyan, T)
        cv2.line(frame, (20, 240), (20, 240 - L), cyan, T)

        cv2.line(frame, (340, 240), (340 - L, 240), cyan, T)
        cv2.line(frame, (340, 240), (340, 240 - L), cyan, T)

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, "ATLAS", (42, 60), cv2.FONT_HERSHEY_DUPLEX, 1, cyan, 2)

        pulse = 0.7 + 0.3 * math.sin(self.tick / 12)

        status = (int(255 * pulse), 255, 0)

        cv2.putText(frame, "STATUS : ONLINE", (40, 95), font, 0.55, status, 2)
        cv2.putText(frame, f"FPS : {int(state.fps)}", (40, 125), font, 0.55, cyan, 2)
        cv2.putText(frame, f"FACES : {state.faces}", (40, 155), font, 0.55, cyan, 2)

        cv2.putText(
            frame,
            datetime.now().strftime("%H:%M:%S"),
            (40, 185),
            font,
            0.55,
            cyan,
            2
        )

        cv2.putText(frame, f"VOICE : {state.voice}", (40, 215), font, 0.55, cyan, 2)

        cv2.line(frame, (0, 8), (w, 8), cyan, 2)

        cv2.putText(
            frame,
            "ATLAS VISION ENGINE",
            (w - 250, 35),
            font,
            0.6,
            cyan,
            2
        )

        # Draw target brackets
        for (x, y, fw, fh) in detections:
            self.draw_target(frame, x, y, fw, fh)

        return frame