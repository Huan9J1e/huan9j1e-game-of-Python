import sys
from time import sleep


import pygame

from Game_Model import Bullet

from Game_Model import GameSetting,Ship,Alien,GameStatus,Button
import Game_Function as gf
from pygame.sprite import Group

        

def rungame():
	  Gameset=GameSetting(800,600,(250,250,250))
	  pygame.init()
	  screen=pygame.display.set_mode(
	    (Gameset.screenW,Gameset.screenH))
	  pygame.display.set_caption('huan9j1e Game')
	  
	  ship=Ship(screen)
	  
	  Gameset.bullet_w=10
	  Gameset.bullet_h=5
	  Gameset.bullet_speed=1
	  bullets=Group()
	  
	  Gameset.alien_speed=100
	  Gameset.alien_drop_speed=100
	  aliens=Group()
	  
	  gf.create_fleet(Gameset,screen,aliens,ship)
	  
	  status=GameStatus(Gameset)
	  
	  pbutton=Button(Gameset,screen,"Play")
	  
	  while True:
	  	gf.check_event(ship,Gameset,screen,bullets,status,pbutton)
	  
	  	
	  	if status.game_active:
	  	    gf.update_bullet(bullets,Gameset,screen,ship,aliens)
	  	
	  	    if(Gameset.delay%200==0):
	  	        gf.update_aliens(Gameset,screen,aliens,ship,bullets,status)    
	  	
	  	    if(Gameset.delay%2==0):	
	  	        ship.move_step(Gameset)
	  	    
	  	    Gameset.delay+=1
	  	    if(Gameset.delay==10000):
	  	        Gameset.delay=0 
	  	        
	  	gf.mouse_en_disable(status)
	  	gf.update_screen(Gameset,screen,ship,bullets,aliens,status,pbutton)

rungame()	  		  	  
