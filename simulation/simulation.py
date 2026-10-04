import numpy as np
from .agent import SeedHandler

class Simulation:
    def __init__(self):
        self.seed = SeedHandler(1000)

    def tick(self):
        self.seed.tick()

    def getSeedPos(self):
        return self.seed.pos[:self.seed.count]

    def addSeed(self, pos, vel=np.zeros(3), acc=np.zeros(3)):
        self.seed.add(pos, vel, acc)