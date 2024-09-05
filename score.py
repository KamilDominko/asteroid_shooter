import pygame as pg
from settings import *


class Score:
    def __init__(self):
        self.font = pg.font.Font("graphics/subatomic.ttf", 50)

    def display(self, display):
        score_text = f"Score: {pg.time.get_ticks() // 1000}"
        text_surf = self.font.render(score_text, False, "White")
        text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
        # pg.display.get_surface().blit(text_surf, text_rect)
        # pg.draw.rect(pg.display.get_surface(), "White", text_rect.inflate(30, 30), width=5, border_radius=5)
        display.blit(text_surf, text_rect)
        pg.draw.rect(display, "White", text_rect.inflate(30, 30), width=5, border_radius=5)
