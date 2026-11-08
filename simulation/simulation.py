import numpy as np
from .agent import SeedHandler
from .field import MonomerHandler

class Simulation:
    def __init__(self):
        self.SPACE_SIZE = 1000

        self.seed = SeedHandler(self, 10000)
        self.monomer = MonomerHandler(10, (100, 100, 100))

    def tick(self):
        self.seed.tick()
        self.monomer.tick()

    def getSeedPos(self):
        return self.seed.pos[:self.seed.count]

    def getSeedLength(self):
        return self.seed.length[:self.seed.count]

    def addSeed(self, pos, vel=np.zeros(3), acc=np.zeros(3), length=0):
        self.seed.add(pos, vel, acc, length)

    def getConcentrationGrid(self):

        return self.monomer.c

