import pygame as pg 
from input_box import InputBox 
from constants import * 

MSG_FONT = pg.font.SysFont(DEFAULT_FONT, DEFAULT_FONT_SIZE)
class InfoBox(InputBox):
    '''static info box''' 
    def __init__(self, x, y, w, h, text='', text_color=PASTEL_PURPLE):
        h = int(h * (len(text.split("\n"))+1)/2)
        super().__init__(x, y, w, h, text=text)
        self.text_color = text_color
        
    def handle_event(self, event=None):
        '''override the handle_event method to do nothing'''
        pass 
    
    def update(self, event=None): 
        '''override update method to do nothing'''
        pass 

    def draw(self, screen):
        
        # Blit the text
        y_offset = 0
        for line in self.text.split('\n'):
            self.txt_surface = MSG_FONT.render(line, True, self.text_color)
            screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + y_offset))
            y_offset += 18
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2) 

