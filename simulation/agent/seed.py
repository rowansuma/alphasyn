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

    def elongate(self): # TODO: Multiple seeds can occupy same cell and make c go negative - fix
        m = self.sim.monomer
        grid_cell = self.grid_cell().astype(int)
        mask = m.get_c(grid_cell) > self.R_ELON

        self.length[mask] += self.R_ELON

        m.add_c(grid_cell[mask], -self.R_ELON)

    def grid_cell(self):
        cfg = self.sim.config["monomer"]
        cells = ((self.pos + self.sim.SPACE_SIZE/2)//cfg["dx"]).astype(int)
        return np.clip(cells, 0, self.sim.monomer.size[0] - 1)

    def tick(self):
        super().tick()
        self.elongate()