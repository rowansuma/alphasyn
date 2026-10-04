from simulation.agent import MovingParticleHandler


class SeedHandler(MovingParticleHandler):
    def __init__(self, MAX_COUNT):
        super().__init__(MAX_COUNT)