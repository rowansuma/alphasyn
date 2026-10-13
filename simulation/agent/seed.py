import numpy as np

from simulation.agent import MovingParticleHandler


class SeedHandler(MovingParticleHandler):
    def __init__(self, sim, MAX_COUNT):
        super().__init__(sim, MAX_COUNT)

        self.R_ELON = 0.5

        self.length = np.zeros(self.MAX_COUNT)

    def add(self, pos, vel=np.zeros(3), acc=np.zeros(3), length=0):
        super().add(pos, vel, acc)
        self.length[self.count-1] = length

    def tick(self):
        super().tick()
        self.length += self.R_ELON