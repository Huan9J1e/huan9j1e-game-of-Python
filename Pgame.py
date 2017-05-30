import sys


import pygame

from Game_Model import Bullet

from Game_Model import GameSetting,Ship,Alien,GameStatus
import Game_Function as gf
from pygame.sprite import Group

        

def rungame():
	  Gameset=GameSetting(800,600,(250,250,250))
	  pygame.init()
	  screen=pygame.display.set_mode(
	    (Gameset.screenW,Gameset.screenH))
	  pygame.display.set_caption('huan9j1e Game')
	  
	  ship=Ship(screen)
	  
	  Gameset.bullet_w=100
	  Gameset.bullet_h=5
	  Gameset.bullet_speed=10
	  bullets=Group()
	  
	  Gameset.alien_speed=50
	  Gameset.alien_drop_speed=50
	  aliens=Group()
	  
	  gf.create_fleet(Gameset,screen,aliens,ship)
	  
	  status=GameStatus(Gameset)
	  
	  while True:
	  	gf.check_event(ship,Gameset,screen,bullets)
	  	
	  	gf.update_bullet(bullets,Gameset,screen,ship,aliens)
	  	
	  	if(Gameset.delay%200==0):
	  	    gf.update_aliens(Gameset,screen,aliens,ship,bullets,status)    
	  	
	  	if(Gameset.delay%2==0):	
	  	    ship.move_step(Gameset)
	  	    
	  	Gameset.delay+=1
	  	if(Gameset.delay==10000):
	  	    Gameset.delay=0           
	 
	  	gf.update_screen(Gameset,screen,ship,bullets,aliens)

rungame()	  		  	  
