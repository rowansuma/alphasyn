from simulation import Simulation
from simulation.ui import UI
import numpy as np

sim = Simulation()

rng = np.random.default_rng()

NUM_SEEDS = 10000

pos = rng.uniform(-500, 500, (NUM_SEEDS, 3))
vel = rng.uniform(-1, 1, (NUM_SEEDS, 3))
acc = np.zeros((NUM_SEEDS, 3))
length = rng.normal(loc=400.0, scale=150.0, size=NUM_SEEDS)

sim.seed.pos = pos
sim.seed.vel = vel
sim.seed.acc = acc
sim.seed.length = length
sim.seed.count = NUM_SEEDS

ui = UI(sim)

while not ui.closed:
    sim.tick()
    ui.update()