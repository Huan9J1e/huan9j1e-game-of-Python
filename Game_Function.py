import sys
from time import sleep

import pygame

from Game_Model import Bullet,Alien


def game_init(status,scoreb,gameset):
	   status.game_active=True
	   status.ships_left=gameset.ship_limit
	   status.score=0
	   scoreb.prep_score()
	   scoreb.prep_ships()

def check_keydown_event(event,ship,gameset,screen,bullets,status,scoreb):
	   if event.key==pygame.K_RIGHT:
	  		  ship.keep_right_moving=True  
	   elif event.key==pygame.K_LEFT:
	  		  ship.keep_left_moving=True
	   elif event.key==pygame.K_SPACE:
	   	    gameset.bullet_keepnew=True
	   elif event.key==pygame.K_q:
	        sys.exit()
	   elif event.key==pygame.K_s:
	   	    if(not status.game_active):
	   	    	game_init(status,scoreb,gameset)
	   elif event.key==pygame.K_UP:
	   	    ship.keep_up_moving=True    	
	   elif event.key==pygame.K_DOWN:
	   	    ship.keep_down_moving=True	         	    
	   	    
	   	   	  	

def check_keyup_event(event,ship,gameset,screen,bullets):
	   if event.key==pygame.K_RIGHT:
	  		  ship.keep_right_moving=False  
	   elif event.key==pygame.K_LEFT:
	  		  ship.keep_left_moving=False	
	   elif event.key==pygame.K_SPACE:
	   	    gameset.bullet_keepnew=False
	   	    newBullet=Bullet(gameset,screen,ship)
	   	    bullets.add(newBullet)
	   elif event.key==pygame.K_UP:
	   	    ship.keep_up_moving=False    	
	   elif event.key==pygame.K_DOWN:
	   	    ship.keep_down_moving=False	    		    		  

#
def check_button_click(gameset,status,pbutton,mouse_x,mouse_y,scoreb):
	  if pbutton.rect.collidepoint(mouse_x,mouse_y)and(not status.game_active):
	  	  game_init(status,scoreb,gameset)
	  	  
	  	  

#
def check_event(ship,gameset,screen,bullets,status,pbutton,scoreb):
	  #event to close pressing the red X button
	  	for event in pygame.event.get():
	  		  if event.type==pygame.MOUSEBUTTONDOWN:
	  		  	  mouse_x,mouse_y=pygame.mouse.get_pos()
	  		  	  check_button_click(gameset,status,pbutton,mouse_x,mouse_y,scoreb)
	  		  	  
	  		  elif event.type==pygame.QUIT:
	  		  	  sys.exit() 
	  		  elif event.type==pygame.KEYDOWN:
	  		  	  #{
	  		  	 	check_keydown_event(event,ship,gameset,screen,bullets,status,scoreb) 
	  		  elif event.type==pygame.KEYUP:
	  		  	  check_keyup_event(event,ship,gameset,screen,bullets)	   
              
#	  		  		    
def update_screen(gameset,screen,ship,bullets,aliens,status,pbutton,scoreb):        
    screen.fill(gameset.bgcolor)
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    if not status.game_active:
    	  pbutton.draw_button()
    	  
    scoreb.show_score()	  
    	  
    pygame.display.flip()
    

#
def get_number_rows(gameset,ship_height,alien_height):
    available_space_y=(gameset.screenH-(3*alien_height)-ship_height)
    number_row=int(available_space_y/(2*alien_height))
    return number_row-2    


#
def get_number_aliens(gameset,alien_width):
    available_space_x=gameset.screenW-2*alien_width
    Naliens=int(available_space_x/(2*alien_width))
    return Naliens
    
def create_alien(gameset,screen,aliens,alienN,row_number):
    alien=Alien(gameset,screen)
    alien_width=alien.rect.width 
    alien.x=alien_width+2*alien_width*alienN
    alien.rect.x=alien.x
    
    alien.rect.y=2*alien.rect.height+2*alien.rect.height*row_number
    
    aliens.add(alien)    

def create_fleet(gameset,screen,aliens,ship):
    alien=Alien(gameset,screen)
    Naliens=get_number_aliens(gameset,alien.rect.width)
    Naliens_y=get_number_rows(gameset,ship.rect.height,alien.rect.height)
    
    for alienN_y in range(Naliens_y):
        for alienN in range(Naliens):
            create_alien(gameset,screen,aliens,alienN,alienN_y) 

#
def change_fleet_direction(gameset,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=gameset.alien_drop_speed
    gameset.direction_x*=-1    

#
def check_fleet_edges(gameset,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(gameset,aliens)
            break

#
def ship_hit(gameset,screen,aliens,ship,bullets,status,scoreb):
    
    status.ships_left-=1
    scoreb.prep_ships()
    if(status.ships_left==0):
        status.game_active=False    
    
    aliens.empty()
    bullets.empty()
    
    create_fleet(gameset,screen,aliens,ship)
    
    ship.center_ship()
    
    sleep(0.5)
    
#
def check_alens_bottom(gameset,screen,aliens,ship,bullets,status,scoreb):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
           ship_hit(gameset,screen,aliens,ship,bullets,status,scoreb)
           break               
#
def update_aliens(gameset,screen,aliens,ship,bullets,status,scoreb):
    check_fleet_edges(gameset,aliens)
    aliens.update() 
    
    if(pygame.sprite.spritecollideany(ship,aliens)):
        ship_hit(gameset,screen,aliens,ship,bullets,status,scoreb)
    
    check_alens_bottom(gameset,screen,aliens,ship,bullets,status,scoreb)
    
#
def renew_aliens(gameset,screen,aliens,ship,bullets):
    if(len(aliens)==0):
       bullets.empty()
       create_fleet(gameset,screen,aliens,ship)
       
#
def update_bullet(bullets,gameset,screen,ship,aliens,scoreb,status):
    bullets.update()
    
	  	  #print(len(bullets))
	  #below is to check when to new a bullet	  
    if(gameset.bullet_keepnew)and(gameset.delay%100==0)and(len(bullets)<gameset.bullet_allow):
    	  newBullet=Bullet(gameset,screen,ship)
    	  bullets.add(newBullet) 
    	  
    #delete the miss bullet
    for bullet in bullets.copy():
	      if bullet.rect.bottom<=0:
	  	      bullets.remove(bullet)	  
    	  
    check_bullet_alien_collisions(gameset,screen,aliens,ship,bullets,scoreb,status)

#    
def check_bullet_alien_collisions(gameset,screen,aliens,ship,bullets,scoreb,status):
    #check if hit
    collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)
    
    if(collisions):
    	   for collinsion in collisions.values():
    	       status.score += gameset.alien_score*len(collinsion)
    	       scoreb.prep_score()
    
    #renew the aliens
    renew_aliens(gameset,screen,aliens,ship,bullets) 
    
#
def mouse_en_disable(status):
	  if(status.game_active):
	  	  pygame.mouse.set_visible(False)
	  else:
	  	  pygame.mouse.set_visible(True)	                                      		  	  