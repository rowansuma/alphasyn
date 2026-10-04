from simulation import Simulation
from simulation.ui import UI
import numpy as np

sim = Simulation()

rng = np.random.default_rng()
for i in range(500):
    sim.addSeed(rng.uniform(-10, 10, 3), rng.uniform(-1, 1, 3))

ui = UI(sim)

while not ui.closed:
    sim.tick()
    ui.update()