import numpy as np

class MonomerHandler:
    def __init__(self, sim):
        self.sim = sim
        # config
        cfg = self.sim.config["monomer"]
        self.dx = cfg["dx"]
        self.D = cfg["diffusion_constant"] # Diffusion Coefficient
        self.dt = self.sim.DT

        length = self.sim.SPACE_SIZE//self.dx
        self.size = (length, length, length)
        self.c = np.zeros(self.size)

        # stability check
        if (self.D * self.dt / (self.dx**2)) > 1/6:
            raise ValueError(f"Diffusion is unstable: {(self.D * self.dt / (self.dx**2))} > 0.1667")

    def get_laplacian(self):
        c = self.c
        return ( c[2:, 1:-1, 1:-1]
                +c[:-2, 1:-1, 1:-1]
                +c[1:-1, 2:, 1:-1]
                +c[1:-1, :-2, 1:-1]
                +c[1:-1, 1:-1, 2:]
                +c[1:-1, 1:-1, :-2]
                -6*c[1:-1,1:-1,1:-1]
            ) / self.dx**2

    def get_c(self, pos): # returns concentrations for each position given a position array
        return self.c[
            pos[:, 0],
            pos[:, 1],
            pos[:, 2]
        ]

    def add_c(self, pos, x): # adds concentrations at each position given a position array
        np.add.at(self.c, (pos[:, 0], pos[:, 1], pos[:, 2]), x)

    def fill_uniform(self, c):
        self.c.fill(c)

    def set(self, pos, c):
        self.c[pos] = c

    def tick(self):
        c_next = self.c.copy()

        c_next[1:-1, 1:-1, 1:-1] += self.D * self.dt * self.get_laplacian()

        self.c = c_next.copy()