import numpy as np

from simulation.agent import ParticleHandler


class MovingParticleHandler(ParticleHandler):
    def __init__(self, MAX_COUNT):
        super().__init__(MAX_COUNT)

        self.vel = np.zeros((self.MAX_COUNT, 3))
        self.acc = np.zeros((self.MAX_COUNT, 3))

    def add(self, pos, vel=np.zeros(3), acc=np.zeros(3)):
        super().add(pos)
        self.vel[self.count-1] = vel
        self.acc[self.count-1] = acc

    def tick(self):
        super().tick()
        self.pos += self.vel
        self.vel += self.acc