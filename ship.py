import pygame as pg

from settings import *
from laser import Laser


class Ship(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pg.image.load("graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.can_shoot = True
        self.last_shoot = 0

    def input_position(self):
        self.rect.center = pg.mouse.get_pos()

    def laser_shoot(self, laser_group):
        if pg.mouse.get_pressed()[0]:
            if self.can_shoot:
                Laser(laser_group, self.rect.midtop)
                self.can_shoot = False
                self.last_shoot = pg.time.get_ticks()
            elif not self.can_shoot and pg.time.get_ticks() - self.last_shoot > 1000:
                self.can_shoot = True

    def update(self, laser_group):
        self.input_position()
        self.laser_shoot(laser_group)
