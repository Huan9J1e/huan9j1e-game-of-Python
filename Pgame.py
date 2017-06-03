import sys
from time import sleep


import pygame

from Game_Model import Bullet,Scoreboard

from Game_Model import GameSetting,Ship,Alien,GameStatus,Button
import Game_Function as gf
from pygame.sprite import Group

        

def rungame():
	  gameset=GameSetting(800,600,(250,250,250))
	  pygame.init()
	  screen=pygame.display.set_mode(
	    (gameset.screenW,gameset.screenH))
	  pygame.display.set_caption('huan9j1e Game')
	  
	  ship=Ship(screen,gameset)
	  
	  gameset.bullet_w=100
	  gameset.bullet_h=5
	  gameset.bullet_speed=1
	  bullets=Group()
	  
	  gameset.alien_speed=5
	  gameset.alien_drop_speed=5
	  aliens=Group()
	  
	  gf.create_fleet(gameset,screen,aliens,ship)
	  
	  status=GameStatus(gameset)
	  
	  pbutton=Button(gameset,screen,"Play")
	  
	  scoreb=Scoreboard(gameset,screen,status)
	  
	  while True:
	  	gf.check_event(ship,gameset,screen,bullets,status,pbutton,scoreb)
	  
	  	
	  	if status.game_active:
	  	    gf.update_bullet(bullets,gameset,screen,ship,
	  	        aliens,scoreb,status)
	  	
	  	    if(gameset.delay%200==0):
	  	        gf.update_aliens(gameset,screen,aliens,ship,bullets,status,scoreb)    
	  	
	  	    if(gameset.delay%2==0):	
	  	        ship.move_step(gameset)
	  	    
	  	    gameset.delay+=1
	  	    if(gameset.delay==10000):
	  	        gameset.delay=0 
	  	        
	  	gf.mouse_en_disable(status)
	  	gf.update_screen(gameset,screen,ship,bullets,
	  	    aliens,status,pbutton,scoreb)

rungame()	  		  	  
