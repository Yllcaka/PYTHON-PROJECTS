import pygame

white = (206, 153, 255)

def circle(x,y,d):
    pygame.draw.circle(screen,white,(x,y),d,1)
    if d>2:
        circle(x+d,y,d//2)
        circle(x-d,y,d//2)
        circle(x,y+d,d//2)
        circle(x,y-d,d//2)

pygame.init()
width,height = 1000,800
screen = pygame.display.set_mode((width,height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    circle(width//2,height//2,200)
    pygame.display.flip()
