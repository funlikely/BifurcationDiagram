'''
    Bifurcation Diagram
'''

import pygame
from math import cos
import sys

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
                y = f(x)
                iy = int( 600 * (1-y))
                screen.set_at((ix, iy), (255,255,255))

                pygame.display.update()


            
            redraw = False
    
def f(x):
    return cos(x)                





if __name__ == '__main__':
    main()

