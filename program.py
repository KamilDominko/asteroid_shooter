import sys
import pygame
from settings import *
from ship import Ship

pygame.init()


class Program:
    def __init__(self):
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.clock = pygame.time.Clock()
        self.running = True

        self.ship_group = pygame.sprite.Group()
        self.player = Ship(self.ship_group)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.ship_group.draw(self.display)
            pygame.display.update()


if __name__ == '__main__':
    Program().run()
