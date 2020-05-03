import pygame, copy, ctypes
import random as r
from time import sleep
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
def make2dArray(col,row):
    return [[None for i in range(row)] for i in range(col)]
def firstArray(col,row):
    return [[r.randint(0,1) for i in range(row)] for i in range(col)]
        
def fate(spot,x,y,cols,rows):
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            try: 
                col = x+i
                row = y+j
                sum+= spot[col][row]
            except:
                continue
    sum -= spot[x][y]
    if spot[x][y] == 0 and sum == 3:
        return 1
    elif spot[x][y] == 1 and (sum <2 or sum >3):
        return 0
    else:
        return spot[x][y]

pygame.init()
cols = 0
rows = 0
resolution = 10
m = 1

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

width,height = screensize
cols = width//resolution
rows = height//resolution
life = firstArray(cols,rows)
windowSize = (width-m,height-m)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("Game of Life")

running = True
current = make2dArray(cols,rows)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    for i in range(cols):
        for j in range(rows):
            currentBeing = life[i][j]
            color = white
            if currentBeing == 1:
                color = black
            x = i*resolution
            y = j*resolution
            pygame.draw.rect(screen,color,[x,y,resolution-m,resolution-m])
    for i in range(cols):
        for j in range(rows):
            current[i][j] = fate(life,i,j,cols,rows)
    # sleep(0.05)
    life = copy.deepcopy(current)
   
    pygame.display.flip()