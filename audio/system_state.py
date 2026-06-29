from audio.state import VoiceState


class SystemState:

    def __init__(self):

        self.voice = VoiceState.STANDBY

        self.faces = 0

        self.fps = 0

        self.active = False

    def set_voice(self, state):

        self.voice = state

    def set_faces(self, faces):

        self.faces = faces

    def set_fps(self, fps):

        self.fps = fps

    def activate(self):

        self.active = True

        self.voice = VoiceState.ACTIVATED


    def deactivate(self):

        self.active = False

        self.voice = VoiceState.STANDBY


STATE = SystemState()