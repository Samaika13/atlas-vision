import cv2
import time

from core.config import WINDOW_TITLE, MIRROR_CAMERA, CAMERA_INDEX
from vision.face_detector import FaceDetector


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.detector = FaceDetector()

        self.prev_time = time.time()

    def draw_reticle(self, frame, x, y, w, h):

        color = (255, 200, 0)

        thickness = 2

        length = 25

        # Top Left
        cv2.line(frame, (x, y), (x + length, y), color, thickness)
        cv2.line(frame, (x, y), (x, y + length), color, thickness)

        # Top Right
        cv2.line(frame, (x + w, y), (x + w - length, y), color, thickness)
        cv2.line(frame, (x + w, y), (x + w, y + length), color, thickness)

        # Bottom Left
        cv2.line(frame, (x, y + h), (x + length, y + h), color, thickness)
        cv2.line(frame, (x, y + h), (x, y + h - length), color, thickness)

        # Bottom Right
        cv2.line(frame, (x + w, y + h), (x + w - length, y + h), color, thickness)
        cv2.line(frame, (x + w, y + h), (x + w, y + h - length), color, thickness)

    def start(self):

        while True:

            ret, frame = self.cap.read()

            if not ret:
                break

            if MIRROR_CAMERA:
                frame = cv2.flip(frame, 1)

            detections = self.detector.detect(frame)

            for (x, y, w, h, conf) in detections:

                self.draw_reticle(frame, x, y, w, h)

                cv2.putText(
                    frame,
                    f"Confidence: {conf:.2f}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 200, 0),
                    2
                )

            current = time.time()

            fps = 1 / (current - self.prev_time)

            self.prev_time = current

            cv2.putText(
                frame,
                "ATLAS • Vision Engine",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 200, 0),
                2
            )

            cv2.putText(
                frame,
                "Sentinel: ACTIVE",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 200, 0),
                2
            )

            cv2.putText(
                frame,
                f"FPS: {int(fps)}",
                (20, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 200, 0),
                2
            )

            cv2.imshow(WINDOW_TITLE, frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()