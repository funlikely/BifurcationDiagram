'''
    Bifurcation Diagram
    2021-01-31

    note- adding the following to settings.json to make pylint behave:
        "python.linting.pylintArgs": [ "--extension-pkg-whitelist=pygame --goodnames=x,y,i,j" ]
'''

import math
import sys
import pygame


def main():
    print('Hello World')

    pygame.init()

    screen = pygame.display.set_mode((600, 600))


    redraw = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()

        if redraw:
            for ix in range(600):
                x = ix / 600
                y_values = bifurcation_values(x)
                iy_values = screenify_y_values(y_values)  # = int( 600 * (1-y))
                for iy in iy_values:
                    screen.set_at((ix, iy), (255,255,255))

                pygame.display.update()


            
            redraw = False
    
def bifurcation_values(x):
    y_values = []

    y_values.append(math.cos(   x))
    y_values.append(math.sin(x))
    return y_values

def screenify_y_values(y_values):
    iy_values = []
    for y in y_values:
        iy_values.append(int(600 * (1-y)))
    return iy_values


if __name__ == '__main__':
    main()


