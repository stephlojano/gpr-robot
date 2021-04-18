import pygame

# Constants
WIDTH, HEIGHT = 900, 500  # Window width and height
GREY = (220,220,220)      # Window color
FPS = 30                  # Window refresh rate

# Create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GPR Robot GUI Controller") # Set window name

def draw_window():
    WIN.fill((GREY))
    pygame.display.update()

# Main Loop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():   # Check for any events
            if event.type == pygame.QUIT:  # Check if user quit the program
                run = False                # Terminate While Loop

        draw_window()

    pygame.quit()


# The following lines mean that only the main function will run if this file is called
# The main function will not run if this file is imported and main is called somewhere else
if __name__ == "__main__":
    main()