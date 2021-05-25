from info_box import InfoBox
import pygame as pg
from constants import *
from datetime import datetime

text_color_mapping = {
    "forward": PINK,
    "left": RED,
    "right": GREEN,
    "backward": BLUE,
    "rotate_left": YELLOW,
    "rotate_right": CCNY_PURPLE,
    "stopped": WHITE,
}

SMALL_FONT = pg.font.SysFont(DEFAULT_FONT, SMALL_FONT_SIZE)


class Console(InfoBox):
    """basically this is a dynamic info box ..."""

    def __init__(self, x, y, w, h, color=BLACK):
        h = int((h * 11) / 2)
        super().__init__(x, y, w, h)
        self.color = color
        self.text_array = []

    def update(self, new_command):
        curr_time = f'[{datetime.now().strftime("%H:%M:%S.%f")}]'
        self.text += f"{curr_time} GPR-Robot is moving {new_command}\n"
        text_only = self.text.split("\n")[:-2]

        for line in text_only:
            self.text_array.append((line, text_color_mapping[line.split()[-1]]))

        if len(self.text_array) > 10:
            self.text = ""
            for line in self.text_array[-10:]:
                self.text += line[0] + "\n"

            self.text_array = []
        # print(self.text_array)

    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect)
        # Blit the text
        y_offset = 0
        for line in self.text_array:
            line_color = line[1]
            self.txt_surface = SMALL_FONT.render(line[0], True, line_color)
            screen.blit(self.txt_surface, (self.rect.x + 10, (self.rect.y) + y_offset))
            y_offset += 16
            # if y_offset >= self.rect.h:
            #     y_offset = 0
            # pg.draw.rect(screen, self.color, self.rect)
