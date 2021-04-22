import pygame as pg 
from constants import * 

pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = PASTEL_PURPLE
COLOR_ACTIVE = PASTEL_BLUE
FONT = pg.font.SysFont('couriernew', 25)
# ARIAL_FONT = pygame.font.SysFont('couriernew', 25)

class InputBox:
    ''' input box for user entry '''
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.text_length = 0
        if self.text:
            self.text_length = len(self.text)
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

        x_text_offset = -1*(SCREEN_SIZE[0]/15)
        y_text_offset = -1 * 0
        self.text_pos_x = x + x_text_offset
        self.text_pos_y = y + y_text_offset
        self.user_entry = ''
        self.user_entry_surface = FONT.render(self.user_entry, True, self.color)
        self.accepted_value = False 
        self.user_fucked_up = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print("user entered " + self.user_entry)
                    if self.user_entry:
                        return self.user_entry
                elif event.key == pg.K_BACKSPACE:
                    self.user_entry = self.user_entry[:-1]
                else:
                    self.user_entry += event.unicode
                # Re-render the text.
                self.user_entry_surface = FONT.render(self.user_entry, True, self.color)
        return None

    def update(self):
        # Resize the box if the text is too long.
        # width = max(200, self.txt_surface.get_width()+10)
        width = max(200, self.user_entry_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        x_text_offset = -1*(SCREEN_SIZE[0]/15)
        y_text_offset = -1 * 0
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + x_text_offset, self.rect.y + y_text_offset))
        screen.blit(self.user_entry_surface, (self.rect.x + 10, self.rect.y + y_text_offset))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()