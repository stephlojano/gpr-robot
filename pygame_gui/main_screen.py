from constants import * 
import pygame as pg 
import time
from os import path, getcwd
from input_box import InputBox
from info_box import InfoBox
from button import Button 
from warnings import warn
from movement_console import Console 
from movement import *

pg.init()
COLOR_INACTIVE = PASTEL_PURPLE
COLOR_ACTIVE = PASTEL_BLUE
COLOR_ACCEPTED = PASTEL_GREEN
COLOR_REJECTED = PASTEL_RED

HEADER_FONT = pg.font.SysFont(DEFAULT_FONT, TITLE_FONT_SIZE)
MSG_FONT = pg.font.SysFont(DEFAULT_FONT, DEFAULT_FONT_SIZE)
SMALL_FONT = pg.font.SysFont(DEFAULT_FONT, SMALL_FONT_SIZE)

CHECK_MARK_IMG = pg.image.load(path.join('.','assets','check_mark.png'))
def draw_first_window(screen):
    screen.fill(BACKGROUND_COLOR)
    header_text = HEADER_FONT.render('Enter Dimensions of Area to be Scanned (in meters)', 1, PASTEL_BLUE)
    screen.blit(header_text, (90,10))

def draw_second_header(screen, dimensions, manual_mode=False):
    color = PASTEL_BLUE
    if manual_mode:
        header_text = f"Controlling Robot in Manual Mode"
        text_surface = HEADER_FONT.render(header_text, 1, color)
        screen.blit(text_surface, (225,10))
    else:
        header_text = f"x: {dimensions[0]} m, y: {dimensions[1]} m, total area: {dimensions[0] * dimensions[1]} m^2"
        text_surface = HEADER_FONT.render(header_text, 1, color)
        screen.blit(text_surface, (120,10))


def draw_bottom_banner(screen):
    robot_img = pg.image.load(path.join('.','assets', 'Robot.png'))
    screen.blit(robot_img, (SCREEN_SIZE[0]-120, SCREEN_SIZE[1]-125))
    credits_text = '''
    Spring 2021 - Senior Design II - GPR Robot
    Mentor: Professor Xiao
    Group: Jenny Li, Stephanie Lojano, Kartik Tyagi, Jorge Yumiseba
    '''
    proj_credits = credits_text.split('\n')
    offset = -75
    for credit in proj_credits:
        text_surface = SMALL_FONT.render(credit, 1, PASTEL_PURPLE)
        screen.blit(text_surface, (5, SCREEN_SIZE[1]+offset))
        offset += 15

def draw_dimension_text(screen, dimensions):
    text = 'Enter Dimensions of Area to be Scanned (in meters)'
    color = PASTEL_BLUE

    if USER_ENTRY_ERROR_CODE in dimensions:
        text = "The value must be a positive number."
        color = PASTEL_RED
    elif None not in dimensions:
        text = f"x: {dimensions[0]} m, y: {dimensions[1]} m, total area: {dimensions[0] * dimensions[1]} m^2"
        color = PASTEL_GREEN

    text_surface = MSG_FONT.render(text, 1, color)
    screen.blit(text_surface, (170, 250))

def manual_move(keys_pressed):
    if keys_pressed[pg.K_w]: # FORWARD
        go_ahead()
        print("GPR Robot is moving forward")
        return "forward"
    elif keys_pressed[pg.K_a]: # LEFT SHIFT
        shift_left()
        print("GPR Robot is shifting left")
        return "left"
    elif keys_pressed[pg.K_s]: # REVERSE
        go_back()
        print("GPR Robot is moving in reverse")
        return "backward"
    elif keys_pressed[pg.K_d]: # RIGHT SHIFT
        shift_right()
        print("GPR Robot is shifting right")
        return "right"
    elif keys_pressed[pg.K_q]: # ROTATE LEFT
        turn_left()
        print("GPR Robot is rotating left")
        return "rotate_left"
    elif keys_pressed[pg.K_e]: # ROTATE RIGHT
        turn_right()
        print("GPR Robot is rotating right")
        return "rotate_right"
    else: 
        stop_car()
        # print("GPR Robot is stopped")
        return "stopped" 

def main():
    print(getcwd())
    screen = pg.display.set_mode(SCREEN_SIZE)
    screen.fill(BACKGROUND_COLOR)
    pg.display.set_caption("GPR Robot GUI Controller")
    clock = pg.time.Clock()
    run = True

    # first screen elements 
    input_x = InputBox(400, 100, 100, 32, text='x = ')
    input_y = InputBox(400, 133, 100, 32, text='y = ')
    manual_button = Button(325, 200, 275, 32, text='Enter Manual Mode')
    user_entry_boxes = [input_x, input_y]
    dimensions = [None, None]
    entries_accepted = [False, False]
    screen_transition_complete = False
    manual_mode = False

    # second screen elements 
    info_box = InfoBox(int((1/16)*SCREEN_SIZE[0]), 50, int((7/8)*SCREEN_SIZE[0]), 32, text=INSTRUCTIONS)
    console = Console(int((1/16)*SCREEN_SIZE[0]), info_box.rect.y + info_box.rect.h + 10, int((7/8)*SCREEN_SIZE[0]), 32)
    
    counter = 0
    while run:
        clock.tick(FRAMERATE)
        counter += 1
        if all(entries_accepted):
            if not screen_transition_complete:
                pg.display.update()
                screen.fill(BACKGROUND_COLOR)
                screen_transition_complete = True

            draw_second_header(screen, dimensions, manual_mode=manual_mode) 
            info_box.draw(screen)
        else:
            draw_first_window(screen)
            

        for event in pg.event.get():   # Check for any events
            if event.type == pg.QUIT:  # Check if user quit the program
                run = False                # Terminate While Loop
            if all(entries_accepted):
                pass 
            else:
                button_clicked = manual_button.handle_event(event)
                if button_clicked:
                    entries_accepted = [True, True]
                    manual_mode = True
                for index, box in enumerate(user_entry_boxes):
                    ret = box.handle_event(event)
                    if ret:
                        try: 
                            ret = float(ret)
                            dimensions[index] = ret
                            entries_accepted[index] = True
                            box.accepted_value = True
                            box.color = COLOR_ACCEPTED
                            if index == 0:
                                screen.blit(CHECK_MARK_IMG, (box.text_pos_x+300, box.text_pos_y-10))
                            else:
                                screen.blit(CHECK_MARK_IMG, (box.text_pos_x+300, box.text_pos_y-42))
                        except: 
                            box.color = COLOR_REJECTED
                            warning_msg = f"The value must be a number. User entered: {ret}"
                            warning_text = MSG_FONT.render(warning_msg, 1, RED)
                            screen.blit(warning_text, (90,250))
                            warn(warning_msg)
                            dimensions[index] = USER_ENTRY_ERROR_CODE

        if all(entries_accepted):
            keys_pressed = pg.key.get_pressed()
            command = manual_move(keys_pressed)
            if counter % 2 == 0:
                console.update(command)
                console.draw(screen) 
        else:
            draw_dimension_text(screen, dimensions)

            for box in user_entry_boxes:
                box.update()

            for box in user_entry_boxes:
                box.draw(screen)
                
            manual_button.draw(screen)
            
        draw_bottom_banner(screen)
        pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    main()
