import pygame
from baseplayer import *

class Player1(BasePlayer):
  def __init__(self):
    super().__init__("Player1", 50, 305, 35, (255, 0, 0), 5)
  
  def key_input(self, key):
    if self.visible == True:
      if key[pygame.K_q] == True:
        self.x_slope = 0
      if key[pygame.K_w] == True:
        self.x_slope = 1
      if key[pygame.K_e] == True:
        self.x_slope = 2
      if key[pygame.K_r] == True:
        self.x_slope = 3
      if key[pygame.K_t] == True:
        self.x_slope = 4
      if key[pygame.K_y] == True:
        self.x_slope = 5
      if key[pygame.K_u] == True:
        self.x_slope = 6
      
      if key[pygame.K_RETURN] == True:
        self.enter_key_down = True
      if key[pygame.K_RETURN] == False and self.enter_key_down:
        self.enter_key_down = False
        self.gamedirector.onEndPlayerTurn(1)
