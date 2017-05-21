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

apple_position = ((0, 0))

FPS = 1000000
fpsClock = pygame.time.Clock()


class Snake:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 1
        self.position = ((self.x, self.y))

    def draw_snake(self):
        pygame.draw.circle(DISPLAYSURF, GREEN, self.position, 10, 0)

    def change_position(self):
        self.position = ((self.x, self.y))

    def snake_delete(self):
        pygame.draw.circle(DISPLAYSURF, BLACK, self.position, 10, 0)

    def move_up(self):
        self.snake_delete()
        self.y -= 10
        self.change_position()
        self.draw_snake()

    def move_down(self):
        self.snake_delete()
        self.y += 10
        self.change_position()
        self.draw_snake()

    def move_right(self):
        self.snake_delete()
        self.x += 10
        self.change_position()
        self.draw_snake()

    def move_left(self):
        self.snake_delete()
        self.x -= 10
        self.change_position()
        self.draw_snake()

    def get_position(self):
        return self.position

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

      
def apple_delete():
    
    pygame.draw.circle(DISPLAYSURF, BLACK, apple_position, 5, 0)
    
    pygame.display.update()
    

                 
def new_apple():
    
    apple_delete()
    
    x_coordinate = random.randint(50, 1230)
    while x_coordinate % 10 != 0:
        x_coordinate = random.randint(50, 1230)
    y_coordinate = random.randint(50, 750)
    while y_coordinate % 10 != 0:
        y_coordinate = random.randint(50, 750)
    
    pygame.draw.circle(DISPLAYSURF, WHITE,\
    (x_coordinate, y_coordinate), 5, 0)
    
    apple_position = ((x_coordinate, y_coordinate))

    pygame.display.update()
    
    return apple_position
     

def game(snake):
    snake_list = snake
    snake_head = snake_list[0]
    for snake in snake_list:
        snake.draw_snake()
    done = False
    apple_position = new_apple()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    for snake in snake_list:
                        snake.move_up()
                if event.key == K_DOWN:
                    for snake in snake_list:
                        snake.move_down()
                if event.key == K_RIGHT:
                    for snake in snake_list:
                        snake.move_right()
                if event.key == K_LEFT:
                    for snake in snake_list:
                        snake.move_left()
            if snake_head.get_position() == apple_position:
                x = snake_list[-1].get_x()
                y = snake_list[-1].get_y()
                snake_list.append(Snake(x - 10, y))
        pygame.display.update()


    quit()

snake = [Snake(640, 400)]
game(snake)

























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
