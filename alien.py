import sys

import pygame
from pygame.sprite import Sprite
import pygame.font
from pygame.sprite import Group


class Alien(Sprite):
    
    def __init__(self,gameset,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.gameset=	gameset; 
        
        self.image=pygame.image.load('image/alien1.bmp')
        self.rect=self.image.get_rect()
        
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height 
        
        self.x=float(self.rect.x)
        
        self.speed=1
        self.direction_x=5
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.x+=self.gameset.alien_speed*self.gameset.direction_x          
        self.rect.x=self.x 
    
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if(self.rect.right>=screen_rect.right):
            return True
        elif(self.rect.left<=0):
            return True
        else:
        	  return False