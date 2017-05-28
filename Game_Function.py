import sys

import pygame

from Game_Model import Bullet

def check_keydown_event(event,ship,Gameset,screen,bullets):
	   if event.key==pygame.K_RIGHT:
	  		  ship.keep_right_moving=True  
	   elif event.key==pygame.K_LEFT:
	  		  ship.keep_left_moving=True
	   elif event.key==pygame.K_SPACE:
	   	    Gameset.bullet_keepnew=True
	   elif event.key==pygame.K_q:
	        sys.exit()	    
	   	    
	   	   	  	

def check_keyup_event(event,ship,Gameset,screen,bullets):
	   if event.key==pygame.K_RIGHT:
	  		  ship.keep_right_moving=False  
	   elif event.key==pygame.K_LEFT:
	  		  ship.keep_left_moving=False	
	   elif event.key==pygame.K_SPACE:
	   	    Gameset.bullet_keepnew=False		    		  

def check_event(ship,Gameset,screen,bullets):
	  #event to close pressing the red X button
	  	for event in pygame.event.get():
	  		  if event.type==pygame.QUIT:
	  		  	  sys.exit() 
	  		  elif event.type==pygame.KEYDOWN:
	  		  	  #{
	  		  	 	 check_keydown_event(event,ship,Gameset,screen,bullets) 
	  		  elif event.type==pygame.KEYUP:
	  		  	   check_keyup_event(event,ship,Gameset,screen,bullets)			  
              #}
#	  		  		    
def update_screen(Gameset,screen,ship,bullets):        
    screen.fill(Gameset.bgcolor)
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()	  		  	  