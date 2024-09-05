import sys
import pygame as pg

from settings import *
from ship import Ship
from laser import Laser
from meteor import Meteor

pg.init()


class Program:
    def __init__(self):
        self.display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption(GAME_NAME)
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 0
        # Grafika tła.
        self.bg_surf = pg.image.load("graphics/background.png").convert()
        # Grupy Sprite'ów.
        self.ship_group = pg.sprite.GroupSingle()
        self.laser_group = pg.sprite.Group()
        self.meteor_group = pg.sprite.Group()
        # Gracz.
        self.player = Ship(self.ship_group)
        # Meteor Timer.
        self.meteor_timer = pg.event.custom_type()
        pg.time.set_timer(self.meteor_timer, 400)

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        pg.quit()
                        sys.exit()
                if event.type == self.meteor_timer:
                    Meteor(self.meteor_group)

            # Update.
            self.ship_group.update(self.laser_group)
            self.laser_group.update(self.dt)
            self.meteor_group.update(self.dt)
            # Grafika.
            self.display.blit(self.bg_surf, (0, 0))
            self.ship_group.draw(self.display)
            self.laser_group.draw(self.display)
            self.meteor_group.draw(self.display)
            pg.display.update()


if __name__ == '__main__':
    Program().run()
