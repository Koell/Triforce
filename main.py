import pygame
import random
import time

X_MIN = 0
Y_MIN = 0
X_MAX = 200
Y_MAX = 200
MAIN_WINDOW_SURFACE = None
# create a pygame.time.Clock object.
window_title = 'Titel'
FPS_CLOCK = pygame.time.Clock()


def initialize_pygame():
    pygame.init()

    # create the game main window.
    main_window_size = (X_MAX, Y_MAX)

    global MAIN_WINDOW_SURFACE
    MAIN_WINDOW_SURFACE = pygame.display.set_mode(main_window_size, pygame.RESIZABLE)
    MAIN_WINDOW_SURFACE.fill(pygame.Color('black'), rect=None)
    pygame.display.update()

    # MAIN_WINDOW_SURFACE = pygame.display.set_mode(main_window_size)

    print('MAIN_WINDOW_SURFACE.get_size() = ', MAIN_WINDOW_SURFACE.get_size())

    # set the window title.

    pygame.display.set_caption(window_title)


def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))


def draw_form(main_cooridates):

    for coordinate in main_cooridates:
        pixel(MAIN_WINDOW_SURFACE, pygame.Color('white'), coordinate)

    random_point = (int(X_MAX / 2), Y_MIN)
    pixel(MAIN_WINDOW_SURFACE, pygame.Color('white'), random_point)
    pygame.display.update()

    run = True
    distance_factor = 0.5
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        random_coordinate = main_cooridates[random.randint(0, len(main_cooridates)-1)]
        random_point = (int(random_point[0] + ((random_coordinate[0] - random_point[0]) * distance_factor)),
                        int(random_point[1] + ((random_coordinate[1] - random_point[1]) * distance_factor)))
        pixel(MAIN_WINDOW_SURFACE, pygame.Color('white'), random_point)
        pygame.display.update()
        #time.sleep(0.0005)


def main():
    initialize_pygame()

    pygame.quit()


if __name__ == "__main__":
    main()
