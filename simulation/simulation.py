import numpy as np
from .agent import SeedHandler

class Simulation:
    def __init__(self):
        self.SPACE_SIZE = 1000

        self.seed = SeedHandler(self, 10000)

    def tick(self):
        self.seed.tick()

    def getSeedPos(self):
        return self.seed.pos[:self.seed.count]

    def getSeedLength(self):
        return self.seed.length[:self.seed.count]

    def addSeed(self, pos, vel=np.zeros(3), acc=np.zeros(3), length=0):
        self.seed.add(pos, vel, acc, length)