import numpy as np
import csv
from pathlib import Path

class MetricHandler:
    def __init__(self, sim, out_path):
        self.sim = sim
        self.seed = sim.seed
        self.monomer = sim.monomer

        self.out_path = Path(out_path)
        self.out_path.parent.mkdir(parents=True, exist_ok=True)

        self.out_file = open(self.out_path, "w", newline="")
        self.writer = csv.writer(self.out_file)

        self.writer.writerow(["step", "seed_count", "monomer_count", "agg_length"])

    def seed_count(self):
        return self.seed.count

    def monomer_count(self):
        return np.sum(self.monomer.c)

    def agg_length(self):
        return np.sum(self.seed.length)

    def save_metrics(self):
        self.writer.writerow([self.sim.step, self.seed_count(), self.monomer_count(), self.agg_length()])
        self.out_file.flush()

    def close(self):
        self.out_file.close()