import pygame, sys, random
from Snake import Snakey
from pygame.locals import *

#Initialize Pygame
pygame.init()

pygame.font.init()
font = pygame.font.Font(None, 48)

#Colors
BLACK = (  0,   0,   0, 255)
WHITE = (255, 255, 255, 255)
RED   = (255,   0,   0 , 255)
GREEN = (  0, 255,   0, 255)
BLUE  = (  0,   0, 255, 255)

#CellWidth
CELLSIZE = 35

#FPS
FPS = 15
fpsClock = pygame.time.Clock()

#Snake
snake = Snakey()
direction = None

#AppleInfo
applePos = [random.randint(0,19),random.randint(0,19)]

DISPLAYSURF = pygame.display.set_mode((700,700))

#Game State
score = 0
end = False

pygame.display.set_caption('Snake     Score: ' + str(score))

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

def collision():
    global direction
    if snake.head()[0] < 0 or snake.head()[0] > 19:
        return True
    if snake.head()[1] < 0 or snake.head()[1] > 19:
        return True
    COLOR = DISPLAYSURF.get_at((snake.head()[0]*CELLSIZE,snake.head()[1]*CELLSIZE))
    if COLOR == GREEN and direction is not None:
        return True
        

def end_game(display):
    display.fill(BLACK)
    text = font.render("Game Over: Play Again(y/n)?", True, WHITE)
    display.blit(text, (124,300))
    pygame.display.update()

def reset(display):
    global score, direction, snake, end
    end = False
    score = 0
    direction = None
    snake = Snakey()
    display.fill(BLACK)
    gameLoop()
    
    

    
def gameLoop():
    global direction, score, end
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
            elif end:
                if pressed[K_y]:
                    reset(DISPLAYSURF)
                if pressed[K_n]:
                    pygame.quit()
                    sys.exit()
        if not end:
            if direction is not None:
                direction()
                if collision():
                    end = True
                    end_game(DISPLAYSURF)
                coverSquare(snake.prevTailPos)
        if not end:
            if snake.head()[0] == applePos[0] and snake.head()[1] == applePos[1]:
                score += 1
                pygame.display.set_caption('Snake     Score: ' + str(score))
                snake.grow()
                drawApple()
            drawSnake()
            #drawGrid()
            pygame.display.update()
            fpsClock.tick(FPS)

gameLoop()


