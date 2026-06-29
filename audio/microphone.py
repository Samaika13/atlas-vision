import numpy as np
import sounddevice as sd

from audio.system_state import STATE
from audio.state import VoiceState

import threading


class Microphone:

    def __init__(self):

        self.stream = sd.InputStream(
            samplerate=16000,
            channels=1,
            callback=self.callback
        )

    def callback(self, indata, frames, time, status):

        volume = np.linalg.norm(indata)

        if STATE.active:
            return

        if volume > 0.03:
            STATE.set_voice(
                VoiceState.LISTENING
            )

        else:
            STATE.set_voice(
            VoiceState.STANDBY
            )

    def start(self):

        self.stream.start()

    def activate(self):

        STATE.activate()

        threading.Timer(
            5,
            STATE.deactivate
        ).start()