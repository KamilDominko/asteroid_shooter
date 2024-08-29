import pygame as pg

from settings import *


class Ship(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pg.image.load("graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def input_position(self):
        self.rect.center = pg.mouse.get_pos()

    def update(self):
        self.input_position()
