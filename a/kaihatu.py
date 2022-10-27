import math
import pygame
from pygame.locals import *
import sys
pygame.init()

x=1500
y=800
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("怪人を倒そう")


player=pygame.transform.scale(pygame.image.load("22026595.png"),(45,45)).convert_alpha()
while(1):
    pygame.display.update()
    for i in range(1,1501,5):
      if ((x/2-45/2)<=1500 or (x/2-45/2)>=0):
        if i%3==0 :
          False
        elif i%2==0:
              False
        elif i%25==0:
            False
        else:
          screen.blit(player,(x/2-45/2,y/2-45/2),player.get_rect())
        x=4*(i-750)
          
           
    

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit(0)