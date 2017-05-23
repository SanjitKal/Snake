class Snakey:
    def __init__(self):
        self.arr = [[10,10]]
        self.size = len(self.arr)
        self.direction = None
        self.prevTailPos = None
    
    def moveRight(self):
        self.arr.insert(0,[self.head()[0]+1,self.head()[1]])
        self.prevTailPos = self.arr.pop()

    def moveUp(self):
        self.arr.insert(0,[self.head()[0],self.head()[1]-1])
        self.prevTailPos = self.arr.pop()

    def moveLeft(self):
        self.arr.insert(0,[self.head()[0]-1,self.head()[1]])
        self.prevTailPos = self.arr.pop()

    def moveDown(self):
        self.arr.insert(0,[self.head()[0],self.head()[1]+1])
        self.prevTailPos = self.arr.pop()

    def grow(self):
        diff = [self.tail()[0]-self.prevTailPos[0],
                self.tail()[1]-self.prevTailPos[1]]
        if diff[0] > 0:
            self.arr.append([self.tail()[0]-1,self.tail()[1]])
        elif diff[0] < 0:
            self.arr.append([self.tail()[0]+1,self.tail()[1]])
        elif diff[1] > 0:
            self.arr.append([self.tail()[0],self.tail()[1]-1])
        elif diff[1] < 0:
            self.arr.append([self.tail()[0],self.tail()[1]+1])

            
    def tail(self):
        return self.arr[len(self.arr)-1]

    def head(self):
        return self.arr[0]
                
        

        
