import numpy as np

from simulation.agent import MovingParticleHandler


class SeedHandler(MovingParticleHandler):
    def __init__(self, sim):
        super().__init__(sim)
        # config
        cfg = self.sim.config["seed"]
        self.R_ELON = cfg["r_elongation"]

        self.length = np.zeros(self.MAX_COUNT)

    def add(self, pos, vel=np.zeros(3), acc=np.zeros(3), length=0):
        super().add(pos, vel, acc)
        self.length[self.count-1] = length

    def tick(self):
        super().tick()
        self.length += self.R_ELON