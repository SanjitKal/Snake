import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake: By Sanjit and Thomas')


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
