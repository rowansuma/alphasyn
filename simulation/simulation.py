import numpy as np
from .agent import SeedHandler
from .field import MonomerHandler

class Simulation:
    def __init__(self, config):
        # config
        self.config = config
        self.SPACE_SIZE = config["general"]["space_size"]
        self.DT = config["general"]["dt"]

        self.seed = SeedHandler(self)
        self.monomer = MonomerHandler(self)

    def tick(self):
        self.seed.tick()
        self.monomer.tick()

    def populateSeeds(self):
        rng = np.random.default_rng()
        cfg = self.config["init"]
        NUM_SEEDS = cfg["num_seeds"]

        self.seed.pos = rng.uniform(-self.SPACE_SIZE/2, self.SPACE_SIZE/2, (NUM_SEEDS, 3))
        self.seed.vel = rng.uniform(-1, 1, (NUM_SEEDS, 3))
        self.seed.acc = np.zeros((NUM_SEEDS, 3))
        self.seed.length = rng.normal(loc=cfg["length_dist_mean"], scale=cfg["length_dist_stdev"], size=NUM_SEEDS)
        self.seed.count = NUM_SEEDS

    def addSeed(self, pos, vel=np.zeros(3), acc=np.zeros(3), length=0):
        self.seed.add(pos, vel, acc, length)

    def getSeedPos(self):
        return self.seed.pos[:self.seed.count]

    def getSeedLength(self):
        return self.seed.length[:self.seed.count]

    def getConcentrationGrid(self):
        return self.monomer.c

