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

        self.plotter.view_xy()
        self.plotter.reset_camera(bounds=(-10, 110, -10, 10, -10, 10))

        self.plotter.show(interactive_update=True)

    def draw_bounds(self):
        box = pv.Cube(
            center=(0, 0, 0),
            x_length=1000,
            y_length=1000,
            z_length=1000
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
