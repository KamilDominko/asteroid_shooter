import pygame as pg
from random import randint, uniform
from settings import *


class Meteor(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pg.image.load('graphics/meteor.png').convert_alpha()
        self.rect = self.image.get_rect(center=(self.__random_pos()))

        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 600)

    def __random_pos(self):
        x = randint(-100, WINDOW_WIDTH + 100)
        y = randint(-150, -50)
        return x, y

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
