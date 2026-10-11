import numpy as np

from simulation.agent import ParticleHandler


class MovingParticleHandler(ParticleHandler):
    def __init__(self, sim, MAX_COUNT):
        super().__init__(sim, MAX_COUNT)

        self.vel = np.zeros((self.MAX_COUNT, 3))
        self.acc = np.zeros((self.MAX_COUNT, 3))

        s = self.sim.SPACE_SIZE/2
        self.min_bounds = np.array([-s, -s, -s])
        self.max_bounds = np.array([s, s, s])

    def add(self, pos, vel=np.zeros(3), acc=np.zeros(3)):
        super().add(pos)
        self.vel[self.count-1] = vel
        self.acc[self.count-1] = acc

    def tick(self):
        super().tick()
        self.pos += self.vel
        self.vel += self.acc
        self.apply_constraints()

    def apply_constraints(self):
        collided_mins = self.pos < self.min_bounds
        collided_maxs = self.pos > self.max_bounds

        self.vel[collided_mins | collided_maxs] *= -1

        self.pos[:] = np.clip(self.pos, self.min_bounds, self.max_bounds)