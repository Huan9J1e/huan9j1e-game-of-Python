import sys

import pygame

from Game_Model import Bullet

from Game_Model import GameSetting,Ship,Alien
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
    if(Gameset.bullet_keepnew)and(Gameset.delay%100==0)and(len(bullets)<Gameset.bullet_allow):
    	  newBullet=Bullet(Gameset,screen,ship)
    	  bullets.add(newBullet)       

def rungame():
	  Gameset=GameSetting(800,600,(250,250,250))
	  pygame.init()
	  screen=pygame.display.set_mode(
	    (Gameset.screenW,Gameset.screenH))
	  pygame.display.set_caption('huan9j1e Game')
	  
	  ship=Ship(screen)
	  
	  bullets=Group()
	  
	  Gameset.alien_speed=10
	  Gameset.alien_drop_speed=30
	  aliens=Group()
	  
	  gf.create_fleet(Gameset,screen,aliens,ship)
	  
	  while True:
	  	gf.check_event(ship,Gameset,screen,bullets)
	  	
	  	update_bullet(bullets,Gameset,screen,ship)
	  	
	  	if(Gameset.delay%200==0):
	  	    gf.update_aliens(aliens,Gameset)    
	  	
	  	if(Gameset.delay%2==0):	
	  	    ship.move_step(Gameset)
	  	    
	  	Gameset.delay+=1
	  	if(Gameset.delay==10000):
	  	    Gameset.delay=0           
	 
	  	gf.update_screen(Gameset,screen,ship,bullets,aliens)

rungame()	  		  	  
