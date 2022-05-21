import pygame as pg
from numba import njit
import numpy as np
import math

height_map_img = pg.image.load('img/height_map.jpg')
height_map = pg.surfarray.array3d(height_map_img)

color_map_img = pg.image.load('img/color_map.jpg')
color_map = pg.surfarray.array3d(color_map_img)

map_height = len(height_map[0])
map_width = len(height_map)


class VoxelRender:
    def __init__(self, app):
        self.app = app
        self.player = app.player
        self.fov = math.pi / 3
        self.h_fov = self.fov / 2
        self.num_rays = app.width
        self.delta_angle = self.fov / self.num_rays
        self.ray_distance = 2000
        self.scale_height = 620
        self.screen_array = np.full((app.width, app.height, 3), (0, 0, 0))

    def update(self):
        self.screen_array = np.random.randint(0, 255, size=self.screen_array.shape)

    def draw(self):
        self.app.screen.blit(pg.surfarray.make_surface(self.screen_array), (0, 0))
