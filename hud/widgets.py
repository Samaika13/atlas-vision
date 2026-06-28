import cv2

from hud.colors import PRIMARY


class LabelWidget:

    def draw(self, frame, label, value, x, y):

        cv2.putText(
            frame,
            label,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            PRIMARY,
            1
        )

        cv2.putText(
            frame,
            value,
            (x + 130, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            PRIMARY,
            2
        )