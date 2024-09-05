import pygame as pg
from random import randint, uniform
from settings import *


class Meteor(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        meteor_image = pg.image.load('graphics/meteor.png').convert_alpha()
        meteor_size = pg.math.Vector2(meteor_image.get_size()) * uniform(0.5, 1.5)
        meteor_transformed = pg.transform.scale(meteor_image, meteor_size).convert_alpha()
        self.original_image = meteor_transformed
        self.image = meteor_transformed
        self.rect = self.image.get_rect(center=(self.__random_pos()))
        self.mask = pg.mask.from_surface(self.image)

        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 600)

        self.rotation = 0
        self.rotation_speed = randint(20, 50)

    def __random_pos(self):
        x = randint(-100, WINDOW_WIDTH + 100)
        y = randint(-150, -50)
        return x, y

    def rotate(self, dt):
        self.rotation += self.rotation_speed * dt
        # rotated_image = pg.transform.rotate(self.original_image, self.rotation).convert_alpha()
        rotated_image = pg.transform.rotozoom(self.original_image, self.rotation, 1).convert_alpha()
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate(dt)
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
