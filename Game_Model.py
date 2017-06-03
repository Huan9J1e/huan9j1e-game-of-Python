import sys

import pygame
from pygame.sprite import Sprite
import pygame.font
from pygame.sprite import Group

from text_type import text_type1_location

#define a class to set the game
class GameSetting():
	   
	   def __init__(self,W=1200,H=800,color=(230,230,230),sizeW=40,ship_speed=1.5):
	   	  self.screenW=W
	   	  self.screenH=H
	   	  self.bgcolor=color
	   	  
	   	  self.ship_speed=ship_speed
	   	  self.ship_updown_speed=1
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
	   	  self.alien_score=5 
	   	     

#
class Ship(Sprite):
    
    def __init__(self,screen,gameset):
    	  super(Ship,self).__init__()
    	  
    	  self.screen=screen
    	  self.gameset=gameset
    	  
    	  self.image=pygame.image.load('image/fly.bmp')
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
    	  		  self.rect.centery= self.rect.bottom; 	  	  
#
class Bullet(Sprite):
	
	  def __init__(self,gameset,screen,ship):
	  	  super(Bullet,self).__init__()
	  	  self.screen=screen
	  	  
	  	  self.rect=pygame.Rect(0,0,gameset.bullet_w,gameset.bullet_h)
	  	  self.rect.centerx=ship.rect.centerx
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
	  	  
#
class Alien(Sprite):
    
    def __init__(self,gameset,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.gameset=	gameset; 
        
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
  
#
class GameStatus():
    def __init__(self,gameset):
        self.gameset=gameset
        self.reset_status()
        
        self.game_active=False
        self.ships_left=self.gameset.ship_limit
        
    def reset_status(self):
        self.ships_left=self.gameset.ship_limit 
        
        self.score=0
        
#
class Button():
	
	  def __init__(self,gameset,screen,msg):
	  	  self.screen=screen
	  	  self.screen_rect=screen.get_rect()
	  	  
	  	  self.width,self.height=200,50
	  	  self.button_color=(0,255,0)
	  	  self.text_color=(255,255,255)
	  	  self.font=pygame.font.Font(text_type1_location,48)
	  	  
	  	  self.rect=pygame.Rect(0,0,self.width,self.height)
	  	  self.rect.center=self.screen_rect.center
	  	  
	  	  self.prep_msg(msg) 
	  	  
	  def prep_msg(self,msg):
	  	  self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
	  	  self.msg_image_rect=self.msg_image.get_rect()	
	  	  self.msg_image_rect.center=self.rect.center  
	  	  
	  def draw_button(self):
	      self.screen.fill(self.button_color,self.rect)
	      self.screen.blit(self.msg_image,self.msg_image_rect)  
	      
#
class Scoreboard():
	  def __init__(self,gameset,screen,status):
	  	  self.screen=screen
	  	  self.screen_rect=screen.get_rect()
	  	  self.gameset=gameset
	  	  self.status=status
	  	  
	  	  self.text_color=(30,30,30)
	  	  self.font=pygame.font.Font(text_type1_location,48)
	  	  
	  	  self.prep_score()
	  	  self.prep_ships()
	  	  
	  def prep_score(self):
	  	  score_str=str(self.status.score)
	  	  self.score_image=self.font.render(score_str,True,
	  	      self.text_color,self.gameset.bgcolor)
	  	  
	  	  self.score_rect=self.score_image.get_rect()
	  	  self.score_rect.right=self.screen_rect.right-5
	  	  self.score_rect.top=5 
	  	  
	  def show_score(self):
	  	  self.screen.blit(self.score_image,self.score_rect)
	  	  
	  	  self.ships.draw(self.screen)
	  	  
	  def prep_ships(self):
	  	  self.ships=Group()
	  	  for shipn in range(self.status.ships_left):
	  	  	  ship=Ship(self.screen,self.gameset)
	  	  	  ship.rect.x=10+shipn*ship.rect.width
	  	  	  ship.rect.y=10
	  	  	  self.ships.add(ship)          	     	  		    