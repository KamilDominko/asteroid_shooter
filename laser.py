import pygame as pg


class Laser(pg.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.image = pg.image.load('graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(0, -1)
        self.speed = 600

    def meteor_collision(self, meteor_group):
        if pg.sprite.spritecollide(self, meteor_group, True):
            self.kill()

    def update(self, dt, meteor_group):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.bottom < 0:
            self.kill()
        self.meteor_collision(meteor_group)
