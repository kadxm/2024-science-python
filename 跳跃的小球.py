import sys
import pygame
pygame.init()
size=width,height=640,480
screen=pygame.display.set_mode(size)
color=(0,0,0)
ball=pygame.image.load('ball.png')
ballrect=ball.get_rect()
speed=[5,5]
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>width:
        speed[1]=-speed[1]
    screen.fill(color)
    screen.blit(ball,ballrect)
    pygame.display.flip()
pygame.quit()