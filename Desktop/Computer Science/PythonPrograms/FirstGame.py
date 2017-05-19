import pygame, sys, random
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1280,800))
pygame.display.set_caption('Snake: By Sanjit and Thomas')

class Snake:
    def __init__(self):
        self.length = 1
        self.position = ((640, 400))
        
        
apple_position = ((0, 0))

        
def apple_delete():
    
    pygame.draw.circle(DISPLAYSURF, BLACK, apple_position, 3, 0)
    
    pygame.display.update()
    
    
                
def new_apple():
    
    apple_delete()
    
    x_coordinate = random.randint(50, 1230)
    y_coordinate = random.randint(50, 750)
    
    pygame.draw.circle(DISPLAYSURF, WHITE,\
    (x_coordinate, y_coordinate), 3, 0)
    
    apple_position = ((x_coordinate, y_coordinate))
    
    pygame.display.update()
    
    return apple_position
     


done = False
while True:
    apple_position = new_apple()
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
