import sys

import pygame
from pygame.sprite import Sprite
import pygame.font
from pygame.sprite import Group

class Ship(Sprite):
    
    def __init__(self,screen,gameset):
    	  super(Ship,self).__init__()
    	  
    	  self.screen=screen
    	  self.gameset=gameset
    	  
    	  self.image=pygame.image.load('image/2fly1.bmp')
    	  self.rect=self.image.get_rect()
    	  self.screen_rect=screen.get_rect()
    	  
    	  self.rect.centerx=self.screen_rect.centerx
    	  self.rect.bottom=self.screen_rect.bottom
    	  
    	  self.keep_right_moving=False 
    	  self.keep_left_moving=False
    	  self.keep_up_moving=False 
    	  self.keep_down_moving=False 
    	  
    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom	
    	  
    def blitme(self):
    	  self.screen.blit(self.image,self.rect)
    	  
    def move_step(self,gameset):
    		
    	  if(self.keep_right_moving)and(self.rect.right<self.screen_rect.right):
    	  	  if(self.rect.right+gameset.ship_speed<self.screen_rect.right):
    	  	      self.rect.centerx +=gameset.ship_speed
    	  	  else:
    	  	  	  self.rect.centerx +=self.screen_rect.right-self.rect.right
    	  	  	  
    	  if(self.keep_left_moving)and(self.rect.left>self.screen_rect.left):
    	  	if(self.rect.left-gameset.ship_speed>self.screen_rect.left):
    	  	    self.rect.centerx -=gameset.ship_speed
    	  	else:
    	  		  self.rect.centerx -=(self.rect.left-self.screen_rect.left)  
    	  
    	  if(self.keep_up_moving)and(self.rect.top>self.screen_rect.top):
    	  	if(self.rect.top-gameset.ship_updown_speed>self.screen_rect.top):
    	  	  	self.rect.centery -=gameset.ship_updown_speed	
    	  	else:
    	  		  self.rect.centery -=(self.rect.top-gameset.ship_updown_speed)
    	  
    	  if(self.keep_down_moving)and(self.rect.bottom<self.screen_rect.bottom):
    	  	if(self.rect.bottom+gameset.ship_updown_speed<self.screen_rect.bottom):
    	  	  	self.rect.centery +=gameset.ship_updown_speed	
    	  	else:
    	  		  self.rect.centery+= (self.rect.bottom-self.rect.bottom); 