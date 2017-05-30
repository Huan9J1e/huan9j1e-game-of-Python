import sys
from time import sleep

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
def ship_hit(Gameset,screen,aliens,ship,bullets,status):
    status.ships_left-=1
    
    aliens.empty()
    bullets.empty()
    
    create_fleet(Gameset,screen,aliens,ship)
    
    ship.center_ship()
    
    sleep(0.5)

#
def check_alens_bottom(Gameset,screen,aliens,ship,bullets,status):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
           ship_hit(Gameset,screen,aliens,ship,bullets,status)
           break               
#
def update_aliens(Gameset,screen,aliens,ship,bullets,status):
    check_fleet_edges(Gameset,aliens)
    aliens.update() 
    
    if(pygame.sprite.spritecollideany(ship,aliens)):
        ship_hit(Gameset,screen,aliens,ship,bullets,status)
    
    check_alens_bottom(Gameset,screen,aliens,ship,bullets,status)
    
#
def renew_aliens(Gameset,screen,aliens,ship,bullets):
    if(len(aliens)==0):
       bullets.empty()
       create_fleet(Gameset,screen,aliens,ship)
       
#
def update_bullet(bullets,Gameset,screen,ship,aliens):
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
    	  
    check_bullet_alien_collisions(Gameset,screen,aliens,ship,bullets)

#    
def check_bullet_alien_collisions(Gameset,screen,aliens,ship,bullets):
    #check if hit
    collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)
    #renew the aliens
    renew_aliens(Gameset,screen,aliens,ship,bullets)                                 		  	  