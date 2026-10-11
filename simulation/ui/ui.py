import numpy as np
import pyvista as pv

from simulation import Simulation

class UI:
    def __init__(self, sim: Simulation):
        self.sim = sim
        self.plotter = pv.Plotter()
        self.cloud = pv.PolyData(self.sim.getSeedPos())

        self.actor = self.plotter.add_mesh(self.cloud, render_points_as_spheres=True, point_size=20)
        self.draw_bounds()

        self.plotter.camera_position = [
            (0, 0, 3000),  # camera pos
            (0, 0, 0),     # focal point
            (0, 1, 0)      # view-up dir
        ]

        self.plotter.show(interactive_update=True)

    def draw_bounds(self):
        box = pv.Cube(
            center=(0, 0, 0),
            x_length=self.sim.SPACE_SIZE,
            y_length=self.sim.SPACE_SIZE,
            z_length=self.sim.SPACE_SIZE
        )

        self.plotter.add_mesh(
            box,
            style="wireframe",
            line_width=2
        )

    @property
    def closed(self):
        return self.plotter._closed

    def update(self):
        self.cloud.points = self.sim.getSeedPos()
        self.plotter.update()  # re-renders and processes window events
