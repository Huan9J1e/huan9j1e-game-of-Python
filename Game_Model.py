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
	   	  self.ship_type=0
	   	  
	   	  self.bullet_speed=1
	   	  self.bullet_w=3 
	   	  self.bullet_h=15
	   	  self.bullet_color=(60,60,60) 
	   	  self.bullet_keepnew=False
	   	  self.bullet_allow=100
	   	  self.bullet_deltax=0 #这个主要是因为2fly类型飞机需要3个子弹 
	   	  
	   	  self.delay=0 
	   	  
	   	  self.alien_speed=1 
	   	  self.alien_drop_speed=1 
	   	  self.direction_x=1 
	   	  self.alien_score=5 
	   	     

#
	  	  
#

      	     	  		    