import sys

import pygame
from pygame.sprite import Sprite

#define a class to set the game
class GameSetting():
	   
	   def __init__(self,W=1200,H=800,color=(230,230,230),sizeW=40,ship_speed=1.5):
	   	  self.screenW=W
	   	  self.screenH=H
	   	  self.bgcolor=color
	   	  
	   	  self.ship_speed=ship_speed
	   	  self.ship_limit=3
	   	  
	   	  self.bullet_speed=1
	   	  self.bullet_w=3
	   	  self.bullet_h=15
	   	  self.bullet_color=(60,60,60) 
	   	  self.bullet_keepnew=False
	   	  self.bullet_allow=10 
	   	  
	   	  self.delay=0 
	   	  
	   	  self.alien_speed=1 
	   	  self.alien_drop_speed=1 
	   	  self.direction_x=1  
	   	     

#
class Ship():
    
    def __init__(self,screen):
    	  
    	  self.screen=screen
    	  
    	  self.image=pygame.image.load('image/fly.bmp')
    	  self.rect=self.image.get_rect()
    	  self.screen_rect=screen.get_rect()
    	  
    	  self.rect.centerx=self.screen_rect.centerx
    	  self.rect.bottom=self.screen_rect.bottom
    	  
    	  self.keep_right_moving=False 
    	  self.keep_left_moving=False 
    	  
    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx	
    	  
    def blitme(self):
    	  self.screen.blit(self.image,self.rect)
    	  
    def move_step(self,Gameset):
    		
    	  if(self.keep_right_moving)and(self.rect.right<self.screen_rect.right):
    	  	  if(self.rect.right+Gameset.ship_speed<self.screen_rect.right):
    	  	      self.rect.centerx +=Gameset.ship_speed
    	  	  else:
    	  	  	  self.rect.centerx +=self.screen_rect.right-self.rect.right
    	  	  	  
    	  if(self.keep_left_moving)and(self.rect.left>self.screen_rect.left):
    	  	if(self.rect.left-Gameset.ship_speed>self.screen_rect.left):
    	  	    self.rect.centerx -=Gameset.ship_speed
    	  	else:
    	  		  self.rect.centerx -=(self.rect.left-self.screen_rect.left)  
    	  		  
#
class Bullet(Sprite):
	
	  def __init__(self,Gameset,screen,ship):
	  	  super(Bullet,self).__init__()
	  	  self.screen=screen
	  	  
	  	  self.rect=pygame.Rect(0,0,Gameset.bullet_w,Gameset.bullet_h)
	  	  self.rect.centerx=ship.rect.centerx
	  	  self.rect.top=ship.rect.top
	  	  
	  	  self.maxT=ship.rect.top;
	  	  
	  	  self.y=float(self.rect.y)
	  	  
	  	  self.color=Gameset.bullet_color
	  	  self.speed=Gameset.bullet_speed 
	  
	  def update(self):
	  	  self.y -= self.speed
	  	  self.rect.y=self.y
	  	  
	  def draw_bullet(self):
	  	  pygame.draw.rect(self.screen,self.color,self.rect)  	
	  	  
#
class Alien(Sprite):
    
    def __init__(self,Gameset,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.Gameset=	Gameset; 
        
        self.image=pygame.image.load('image/alien.bmp')
        self.rect=self.image.get_rect()
        
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height 
        
        self.x=float(self.rect.x)
        
        self.speed=1
        self.direction_x=5
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.x+=self.Gameset.alien_speed*self.Gameset.direction_x          
        self.rect.x=self.x 
    
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if(self.rect.right>=screen_rect.right):
            return True
        elif(self.rect.left<=0):
            return True
        else:
        	  return False        
  
#
class GameStatus():
    def __init__(self,Gameset):
        self.Gameset=Gameset
        self.reset_status()
        
    def reset_status(self):
        self.ships_left=self.Gameset.ship_limit   	     	  		    