import numpy as np
import pyvista as pv

from simulation import Simulation

class UI:
    def __init__(self, sim: Simulation):
        self.sim = sim
        self.plotter = pv.Plotter()

        self.SHOW_SEEDS = True
        self.SHOW_MONOMER = False

        self.cloud = pv.PolyData(self.sim.getSeedPos())
        self.cloud["length"] = self.sim.getSeedLength()

        grid = self.sim.getConcentrationGrid()
        self.MONOMER_DISPLAY_THRESHOLD = 5
        self.cube_cloud = pv.PolyData(np.argwhere(grid > self.MONOMER_DISPLAY_THRESHOLD).astype(float)*self.sim.monomer.dxyz)
        self.cube_cloud["concentration"] = grid[grid > self.MONOMER_DISPLAY_THRESHOLD]

        if self.SHOW_SEEDS:
            self.plotter.add_mesh(self.cloud, scalars="length", cmap="viridis", clim=[0, 1000], render_points_as_spheres=True, point_size=10)

        if self.SHOW_MONOMER:
            glyphs = self.cube_cloud.glyph(
                geom=pv.Cube(x_length=self.sim.monomer.dxyz,
                             y_length=self.sim.monomer.dxyz,
                             z_length=self.sim.monomer.dxyz),
                scale=False,
            )

            self.glyph_actor = self.plotter.add_mesh(
                glyphs,
                scalars="concentration",
                cmap="viridis",
                clim=[0, 100],
                opacity=0.85,
                show_scalar_bar=True
        )


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
        if self.SHOW_SEEDS:
            self.cloud.points = self.sim.getSeedPos()
            self.cloud["length"] = self.sim.getSeedLength()

        if self.SHOW_MONOMER:
            grid = self.sim.getConcentrationGrid()
            self.cube_cloud.points = np.argwhere(grid > self.MONOMER_DISPLAY_THRESHOLD).astype(float)*self.sim.monomer.dxyz-self.sim.SPACE_SIZE/2
            self.cube_cloud["concentration"] = grid[grid > self.MONOMER_DISPLAY_THRESHOLD]

            glyphs = self.cube_cloud.glyph(
                geom=pv.Cube(
                    x_length=self.sim.monomer.dxyz,
                    y_length=self.sim.monomer.dxyz,
                    z_length=self.sim.monomer.dxyz,
                ),
                scale=False,
            )

            self.glyph_actor.mapper.SetInputData(glyphs)

        self.plotter.update()  # re-renders and processes window events
