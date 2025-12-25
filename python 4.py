import pygame, random

pygame.init()
w,h=600,400
s=pygame.display.set_mode((w,h))
c=pygame.time.Clock()

x,y=300,200
dx,dy=10,0
food=[random.randrange(0,w,10),random.randrange(0,h,10)]
snake=[[x,y]]

run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_UP: dx,dy=0,-10
            if e.key==pygame.K_DOWN: dx,dy=0,10
            if e.key==pygame.K_LEFT: dx,dy=-10,0
            if e.key==pygame.K_RIGHT: dx,dy=10,0

    x+=dx; y+=dy
    snake.append([x,y])
    if [x,y]==food:
        food=[random.randrange(0,w,10),random.randrange(0,h,10)]
    else:
        snake.pop(0)

    if x<0 or x>=w or y<0 or y>=h or [x,y] in snake[:-1]:
        run=False

    s.fill((0,0,0))
    for b in snake: pygame.draw.rect(s,(0,255,0),(*b,10,10))
    pygame.draw.rect(s,(255,0,0),(*food,10,10))
    pygame.display.update()
    c.tick(15)

pygame.quit()
