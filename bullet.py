import sys

import pygame
from pygame.sprite import Sprite
import pygame.font
from pygame.sprite import Group


class Bullet(Sprite):
	
	  def __init__(self,gameset,screen,ship):
	  	  super(Bullet,self).__init__()
	  	  self.screen=screen
	  	  
	  	  self.rect=pygame.Rect(0,0,gameset.bullet_w,gameset.bullet_h)
	  	  
	  	  self.rect.centerx=ship.rect.centerx+gameset.bullet_deltax
	  	  self.rect.top=ship.rect.top
	  	  
	  	  self.maxT=ship.rect.top;
	  	  
	  	  self.y=float(self.rect.y)
	  	  
	  	  self.color=gameset.bullet_color
	  	  self.speed=gameset.bullet_speed 
	  
	  def update(self):
	  	  self.y -= self.speed
	  	  self.rect.y=self.y
	  	  
	  def draw_bullet(self):
	  	  pygame.draw.rect(self.screen,self.color,self.rect)  	
	  	  