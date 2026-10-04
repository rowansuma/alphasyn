import numpy as np

class ParticleHandler:
    def __init__(self, MAX_COUNT):
        self.MAX_COUNT = MAX_COUNT

        self.pos = np.zeros((self.MAX_COUNT, 3))
        self.count = 0

    def add(self, pos): # pos: 3x1x1 array
        self.count += 1
        self.pos[self.count-1] = pos

    def tick(self):
        pass