import cv2
from core.config import WINDOW_TITLE, MIRROR_CAMERA, CAMERA_INDEX

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)

    def start(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                break

            if MIRROR_CAMERA:
                frame = cv2.flip(frame, 1)

            cv2.imshow(WINDOW_TITLE, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()