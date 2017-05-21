import random

class Ball:

    #Borders
    RIGHT = 1230
    BOTTOM = 700
    XCENTER = 615
    YCENTER = 350
    
    def __init__(self):
        dirArr = [1,-1]
        self.pos = [random.randint(5,1225),random.randint(5,655)]
        self.direction = [dirArr[random.randint(0,1)],dirArr[random.randint(0,1)]]
        self.speed = [5,5]

    def move(self):
        if self.pos[0]+10 >= self.RIGHT:
            self.direction[0] = -1
        elif self.pos[0]-10 <= 0:
            self.direction[0] = 1
        if self.pos[1]+10 >= self.BOTTOM:
            self.direction[1] = -1
        elif self.pos[1]-10 <= 0:
            self.direction[1] = 1
        self.pos[0] += self.direction[0]*self.speed[0]
        self.pos[1] += self.direction[1]*self.speed[1]
        

