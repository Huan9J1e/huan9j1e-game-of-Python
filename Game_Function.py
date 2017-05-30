import sys

import pygame

from Game_Model import Bullet,Alien

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
def update_screen(Gameset,screen,ship,bullets,aliens):        
    screen.fill(Gameset.bgcolor)
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
    

#
def get_number_rows(Gameset,ship_height,alien_height):
    available_space_y=(Gameset.screenH-(3*alien_height)-ship_height)
    number_row=int(available_space_y/(2*alien_height))
    return number_row-2    


#
def get_number_aliens(Gameset,alien_width):
    available_space_x=Gameset.screenW-2*alien_width
    Naliens=int(available_space_x/(2*alien_width))
    return Naliens
    
def create_alien(Gameset,screen,aliens,alienN,row_number):
    alien=Alien(Gameset,screen)
    alien_width=alien.rect.width 
    alien.x=alien_width+2*alien_width*alienN
    alien.rect.x=alien.x
    
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    
    aliens.add(alien)    

def create_fleet(Gameset,screen,aliens,ship):
    alien=Alien(Gameset,screen)
    Naliens=get_number_aliens(Gameset,alien.rect.width)
    Naliens_y=get_number_rows(Gameset,ship.rect.height,alien.rect.height)
    
    for alienN_y in range(Naliens_y):
        for alienN in range(Naliens):
            create_alien(Gameset,screen,aliens,alienN,alienN_y) 

#
def change_fleet_direction(Gameset,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=Gameset.alien_drop_speed
    Gameset.direction_x*=-1    

#
def check_fleet_edges(Gameset,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(Gameset,aliens)
            break
            
#
def update_aliens(aliens,Gameset):
    check_fleet_edges(Gameset,aliens)
    aliens.update()                   		  	  