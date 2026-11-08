import numpy as np

class MonomerHandler:
    def __init__(self, dxyz, size):
        self.dxyz = dxyz
        self.c = np.zeros(size)
        self.size = size

        self.D = 10 # Diffusion Coefficient
        self.dt = 1

        if (self.D * self.dt / (self.dxyz**2)) > 1/6:
            raise ValueError(f"Diffusion is unstable: {(self.D * self.dt / (self.dxyz**2))} > 0.1667")

    def get_laplacian(self):
        c = self.c
        return ( c[2:, 1:-1, 1:-1]
                +c[:-2, 1:-1, 1:-1]
                +c[1:-1, 2:, 1:-1]
                +c[1:-1, :-2, 1:-1]
                +c[1:-1, 1:-1, 2:]
                +c[1:-1, 1:-1, :-2]
                -6*c[1:-1,1:-1,1:-1]
            ) / self.dxyz**2

    def set(self, pos, c):
        self.c[pos] = c

    def tick(self):
        c_next = self.c.copy()

        c_next[1:-1, 1:-1, 1:-1] += self.D * self.dt * self.get_laplacian()

        self.c = c_next.copy()