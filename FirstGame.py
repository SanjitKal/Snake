import pygame, sys, random
from pygame.locals import *
from ball import Ball
pygame.init()

#Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#FPS
FPS = 300
fpsClock = pygame.time.Clock()

#Balls
balls = []

def init():
    for i in range(0,9):
        b = Ball()
        balls.append(b)

DISPLAYSURF = pygame.display.set_mode((1230,700))
pygame.display.set_caption('Snake: By Sanjit and Thomas')


def draw_balls():
    for b in balls:
        pygame.draw.aacircle(DISPLAYSURF, BLACK, (b.pos[0], b.pos[1]), 10, 0)
        b.move()
        pygame.draw.aacircle(DISPLAYSURF, GREEN, (b.pos[0], b.pos[1]), 10, 0)


def gameLoop():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_balls()
        pygame.display.update()
        fpsClock.tick(FPS)

gameLoop()



















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
