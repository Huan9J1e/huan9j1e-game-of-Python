import sys

import pygame

from Game_Model import Bullet

from Game_Model import GameSetting,Ship
import Game_Function as gf
from pygame.sprite import Group

def update_bullet(bullets,Gameset,screen,ship):
    bullets.update()
    #delete the miss bullet
    for bullet in bullets.copy():
	      if bullet.rect.bottom<=0:
	  	      bullets.remove(bullet)
	  	  #print(len(bullets))
	  #below is to check when to new a bullet	  
    if(Gameset.bullet_keepnew)and(Gameset.delay>100)and(len(bullets)<Gameset.bullet_allow):
    	  newBullet=Bullet(Gameset,screen,ship)
    	  bullets.add(newBullet)
    	  Gameset.delay=0
    Gameset.delay+=1       

def rungame():
	  Gameset=GameSetting(800,600,(250,250,250))
	  pygame.init()
	  screen=pygame.display.set_mode(
	    (Gameset.screenW,Gameset.screenH))
	  pygame.display.set_caption('huan9j1e Game')
	  
	  ship=Ship(screen)
	  
	  bullets=Group()
	  
	  while True:
	  	gf.check_event(ship,Gameset,screen,bullets)
	  	
	  	update_bullet(bullets,Gameset,screen,ship)
	  	
	  	if(Gameset.delay%2==0):	
	  	    ship.move_step(Gameset)        
	 
	  	gf.update_screen(Gameset,screen,ship,bullets)

rungame()	  		  	  
