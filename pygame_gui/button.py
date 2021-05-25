import pygame as pg
from constants import *

FONT = pg.font.SysFont("couriernew", 20)


class Button:
    """Button for navigation"""

    def __init__(self, x, y, w, h, button_color=PASTEL_GREEN, text="", text_color=RED):
        self.rect = pg.Rect(x, y, w, h)
        self.button_color = button_color
        self.text = text
        self.text_color = text_color
        self.text_surface = FONT.render(self.text, True, self.text_color)
        self.clicked = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pg.mouse.get_pos()
                if self.rect.collidepoint((mouse_x, mouse_y)):
                    self.clicked = True

        return self.clicked

    def draw(self, screen):
        pg.draw.rect(screen, self.button_color, self.rect)
        screen.blit(self.text_surface, (self.rect.x + 35, self.rect.y + 5))
