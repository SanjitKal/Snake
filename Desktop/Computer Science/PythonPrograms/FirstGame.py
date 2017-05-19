import pygame, sys
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake: By Sanjit and Thomas')

def new_dot():
    pygame.draw.circle(gameDisplay, WHITE,\
    (random.randint(50, 1230), random.randint(50, 750)), 3, 0)
    pygame.display.update()


done = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

quit()
























##def fib(n):
##    if n == 1:
##        return 0
##    elif n == 2:
##        return 1
##    else:
##        return (fib(n-1) + fib(n-2))
##
##
##print (fib(10))
