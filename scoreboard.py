import sys

import pygame
from pygame.sprite import Sprite
import pygame.font
from pygame.sprite import Group

from ship import Ship

from text_type import text_type1_location


class GameStatus():
    def __init__(self,gameset):
        self.gameset=gameset
        self.reset_status()
        
        self.game_active=False
        self.ships_left=self.gameset.ship_limit
        
    def reset_status(self):
        self.ships_left=self.gameset.ship_limit 
        
        self.score=0

class Scoreboard():
	  def __init__(self,gameset,screen,status):
	  	  self.screen=screen
	  	  self.screen_rect=screen.get_rect()
	  	  self.gameset=gameset
	  	  self.status=status
	  	  
	  	  self.text_color=(30,30,30)
	  	  self.font=pygame.font.Font(text_type1_location,48)
	  	  
	  	  self.prep_score()
	  	  self.prep_ships()
	  	  
	  def prep_score(self):
	  	  score_str=str(self.status.score)
	  	  self.score_image=self.font.render(score_str,True,
	  	      self.text_color,self.gameset.bgcolor)
	  	  
	  	  self.score_rect=self.score_image.get_rect()
	  	  self.score_rect.right=self.screen_rect.right-5
	  	  self.score_rect.top=5 
	  	  
	  def show_score(self):
	  	  self.screen.blit(self.score_image,self.score_rect)
	  	  
	  	  self.ships.draw(self.screen)
	  	  
	  def prep_ships(self):
	  	  self.ships=Group()
	  	  for shipn in range(self.status.ships_left):
	  	  	  ship=Ship(self.screen,self.gameset)
	  	  	  ship.rect.x=10+shipn*ship.rect.width
	  	  	  ship.rect.y=10
	  	  	  self.ships.add(ship) 