from vision.camera import Camera

class AtlasEngine:
    def __init__(self):
        self.camera = Camera()

    def run(self):
        self.camera.start()