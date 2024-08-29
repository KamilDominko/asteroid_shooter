import pygame as pg


class Laser(pg.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.image = pg.image.load('graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
