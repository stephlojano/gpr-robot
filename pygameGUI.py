import pygame
#from movement import *
pygame.font.init()


# Constants
WIDTH, HEIGHT = 900, 500  # Window width and height
GREY = (220,220,220)      # Window color
BLACK = (0,0,0)
FPS = 30                  # Window refresh rate
ARIAL_FONT = pygame.font.SysFont('arial', 40) 

# Create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GPR Robot GUI Controller") # Set window name

def draw_window():
    WIN.fill((GREY))
    header_text = ARIAL_FONT.render('Enter Dimensions of Area to be Scanned', 1, BLACK)
    WIN.blit(header_text, (150,10))
    pygame.display.update()


def manual_move(keys_pressed):
    if keys_pressed[pygame.K_a]: # LEFT SHIFT
        #shift_left()
        print("GPR Robot is shifting left")
    elif keys_pressed[pygame.K_s]: # REVERSE
        #go_back()
        print("GPR Robot is moving in reverse")
    elif keys_pressed[pygame.K_d]: # RIGHT SHIFT
        #shift_right()
        print("GPR Robot is shifting right")
    elif keys_pressed[pygame.K_w]: # FORWARD
        #go_ahead()
        print("GPR Robot is moving forward")
    elif keys_pressed[pygame.K_q]: # ROTATE LEFT
        #turn_left()
        print("GPR Robot is rotating left")
    elif keys_pressed[pygame.K_e]: # ROTATE RIGHT
        #turn_right()
        print("GPR Robot is rotating right")
    else: # STOP
        #stop_car()
        print("GPR Robot has stopped")


# Main Loop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():   # Check for any events
            if event.type == pygame.QUIT:  # Check if user quit the program
                run = False                # Terminate While Loop

        keys_pressed = pygame.key.get_pressed()
        manual_move(keys_pressed)
        draw_window()

    pygame.quit()


# The following lines mean that only the main function will run if this file is called
# The main function will not run if this file is imported and main is called somewhere else
if __name__ == "__main__":
    main()