from simulation import Simulation
from simulation.ui import UI
import tomllib
from pathlib import Path

with open(Path("config.toml"), "rb") as f:
    config = tomllib.load(f)

sim = Simulation(config)
sim.populateSeeds()
sim.monomer.set((50, 50, 50), 100000000)

ui = UI(sim)

while not ui.closed:
    sim.tick()
    ui.update()