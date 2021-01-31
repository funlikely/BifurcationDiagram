'''
    Bifurcation Diagram
    2021-01-31

    note- adding the following to settings.json to make pylint behave:
        "python.linting.pylintArgs": [ "--extension-pkg-whitelist=pygame --goodnames=x,y,i,j" ]
'''

import math
import sys
import pygame


#draw bifurcation diagram
def main():
    print('Hello World')

    pygame.init()
    screen_size = (1200, 800)

    screen = pygame.display.set_mode(screen_size)

    # graph

    redraw = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()

        if redraw:
            for ix in range(screen_size[0]):
                x = ix * 4 / screen_size[0]
                y_values = bifurcation_values(x)
                iy_values = screenify_y_values(y_values, screen_size[1])  # = int( 600 * (1-y))
                for iy in iy_values:
                    screen.set_at((ix, iy), (255,255,255))

                pygame.display.update()

            redraw = False

    
'''returns a set of vertical values for the bifurcation diagram'''
def bifurcation_values(r):
    '''returns a set of vertical values for the bifurcation diagram'''
    y_values = []

    iterations = 300
    sample_threshold = 200

    x = 0.5

    for i in range(iterations):
        x = x * (1-x) * r
        if i > sample_threshold:
            y_values.append(x)

    return y_values


def screenify_y_values(y_values, height):
    '''scales vertical values from the graph to the screen'''
    iy_values = []
    for y in y_values:
        iy_values.append(int(height * (1-y)))
    return iy_values


if __name__ == '__main__':
    main()
