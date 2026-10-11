from simulation.agent import MovingParticleHandler


class SeedHandler(MovingParticleHandler):
    def __init__(self, sim, MAX_COUNT):
        super().__init__(sim, MAX_COUNT)