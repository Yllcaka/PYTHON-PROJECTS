import pygame,ctypes
from time import sleep




class Ant:
    def __init__(self,arr:list,direction:str,x,y):
        self.arr = arr
        self.direction = direction.upper()
        self.x = x
        self.y = y
        self.position = self.arr[self.x][self.y]

    def antPosition(self,dir:str):
        x = self.x
        y = self.y

        Directions = {"UP":(x,y-1),"RIGHT":(x+1,y),"DOWN":(x,y+1),"LEFT":(x-1,y)}
        return Directions[dir]
    
    def changeAntDirection(self,color:int,dir:str):
        DirectionClockWise = {"UPbegin":"RIGHT","RIGHTbegin":"DOWN","DOWNbegin":"LEFT","LEFTbegin":"UP"}
        DirectionCounterClockWise = {"UPbegin":"LEFT","LEFTbegin":"DOWN","DOWNbegin":"RIGHT","RIGHTbegin":"UP"}
        return DirectionCounterClockWise[dir] if color ==1 else DirectionClockWise[dir] 

    def move(self):
        try:
            if self.position == 1:
                self.arr[self.x][self.y] = 0
                self.direction = self.changeAntDirection(1,self.direction+"begin")
                self.x,self.y = self.antPosition(self.direction)
                self.position = self.arr[self.x][self.y]
                
                self.arr[self.x][self.y] =1
            elif self.position == 0:
                self.arr[self.x][self.y] = 1         
                self.direction = self.changeAntDirection(0,self.direction+"begin")
                self.x,self.y = self.antPosition(self.direction)
                self.position = self.arr[self.x][self.y]
        except:
            try:
                self.position = self.arr[len(self.arr) - self.x][len(self.arr) - self.y]
            except:
                self.position = self.arr[0][0]
            





def make2dArray(col,row):
    return [[0 for i in range(col)] for i in range(row)]


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


pygame.init()
cols = 0
rows = 0
resolution = 5
m = 1

width,height = screensize
cols = height//resolution
rows = width//resolution

windowSize = (width-m,height-m)
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

running = True
current = make2dArray(cols,rows)
ANT = Ant(current,"UP",cols-15,rows//3)





current = ANT.arr
screen.fill(black)
for i in range(rows):
        for j in range(cols):
            currentBeing = current[i][j]
            color = white
            if currentBeing == 1:
                color = black
            x = i*resolution
            y = j*resolution
            pygame.draw.rect(screen,color,[x,y,resolution-m,resolution-m])
            pygame.draw.rect(screen,red,[ANT.x*resolution,ANT.y*resolution,resolution-m,resolution-m])
antColor = pygame.draw.rect(screen,red,[ANT.x*resolution,ANT.y*resolution,resolution-m,resolution-m])
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(rows):
        for j in range(cols):
            currentBeing = current[i][j]
            color = black
            if currentBeing != 1:
                continue
            x = i*resolution
            y = j*resolution
            pygame.draw.rect(screen,color,[x,y,resolution-m,resolution-m])
            pygame.draw.rect(screen,white,[ANT.x*resolution,ANT.y*resolution,resolution-m,resolution-m])
            
            
   
    ANT.move()
    antColor = pygame.draw.rect(screen,red,[ANT.x*resolution,ANT.y*resolution,resolution-m,resolution-m])
    current = ANT.arr
    # sleep(1)
    pygame.display.flip()
