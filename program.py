import sys
import pygame as pg
from settings import *
from ship import Ship

pg.init()


class Program:
    def __init__(self):
        self.display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption(GAME_NAME)
        self.clock = pg.time.Clock()
        self.running = True

        self.ship_group = pg.sprite.Group()
        self.player = Ship(self.ship_group)

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
            self.ship_group.draw(self.display)
            pg.display.update()


if __name__ == '__main__':
    Program().run()
