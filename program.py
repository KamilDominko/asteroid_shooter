import sys
import pygame as pg

from settings import *
from ship import Ship
from laser import Laser

pg.init()


class Program:
    def __init__(self):
        self.display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption(GAME_NAME)
        self.clock = pg.time.Clock()
        self.running = True
        # Grafika tła.
        self.bg_surf = pg.image.load("graphics/background.png").convert()
        # Grupy Sprite'ów.
        self.ship_group = pg.sprite.GroupSingle()
        self.laser_group = pg.sprite.Group()
        # Gracz.
        self.player = Ship(self.ship_group)
        self.laser = Laser(self.laser_group, self.player.rect.midtop)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
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
            # Update.
            self.ship_group.update()
            # Grafika.
            self.display.blit(self.bg_surf, (0, 0))
            self.laser_group.draw(self.display)
            self.ship_group.draw(self.display)
            pg.display.update()


if __name__ == '__main__':
    Program().run()
