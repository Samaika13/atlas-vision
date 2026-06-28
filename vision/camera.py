import cv2
import time

from core.config import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    CAMERA_INDEX,
    MIRROR_CAMERA,
)

from hud.renderer import HUDRenderer


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, WINDOW_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, WINDOW_HEIGHT)

        self.prev_time = time.time()

        self.hud = HUDRenderer()

    def start(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            if MIRROR_CAMERA:
                frame = cv2.flip(frame, 1)

            current = time.time()

            fps = 1 / max(current - self.prev_time, 0.0001)

            self.prev_time = current

            # ---------- HUD ----------
            self.hud.render(frame, fps)

            cv2.imshow(WINDOW_TITLE, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()