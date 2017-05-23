import pygame, sys, random
from Snake import Snakey
from pygame.locals import *

#Initialize Pygame
pygame.init()

#Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#CellWidth
CELLSIZE = 35

#FPS
FPS = 60
fpsClock = pygame.time.Clock()

#Snake
snake = Snakey()

#AppleInfo
applePos = [random.randint(0,19),random.randint(0,19)]

DISPLAYSURF = pygame.display.set_mode((700,700))
pygame.display.set_caption('Snake     Score: ')

def drawApple():
    global applePos
    applePos = [random.randint(0,19),random.randint(0,19)]
    pygame.draw.rect(DISPLAYSURF, RED, (applePos[0]*CELLSIZE,applePos[1]*CELLSIZE,CELLSIZE,CELLSIZE), 0)
    
def drawSnake():
    for i in range(len(snake.arr)):
        pygame.draw.rect(DISPLAYSURF, GREEN, (snake.arr[i][0]*CELLSIZE,snake.arr[i][1]*CELLSIZE,CELLSIZE,CELLSIZE), 0)

def coverSquare(loc):
    pygame.draw.rect(DISPLAYSURF, BLACK, (loc[0]*CELLSIZE,loc[1]*CELLSIZE,CELLSIZE,CELLSIZE), 0)

def drawGrid():
    for i in range(20):
        pygame.draw.line(DISPLAYSURF,WHITE,(i*CELLSIZE,0),(i*CELLSIZE,700))
        pygame.draw.line(DISPLAYSURF,WHITE,(0,i*CELLSIZE),(700,i*CELLSIZE))

def gameLoop():
    direction = None
    drawApple()
    drawSnake()
    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif pressed[K_RIGHT]:
                direction = snake.moveRight
            elif pressed[K_LEFT]:
                direction = snake.moveLeft
            elif pressed[K_UP]:
                direction = snake.moveUp
            elif pressed[K_DOWN]:
                direction = snake.moveDown
        if direction is not None:
            coverSquare(snake.tail())
            direction()
        if snake.head()[0] == applePos[0] and snake.head()[1] == applePos[1]:
            snake.grow()
            drawApple()
        drawSnake()
        #drawGrid()
        pygame.display.update()
        fpsClock.tick(FPS)
        


gameLoop()
