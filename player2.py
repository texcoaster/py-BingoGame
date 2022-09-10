import pygame
from baseplayer import *

class Player2(BasePlayer):
  def __init__(self):
    super().__init__("Player2", 50, 305, 35, (0, 255, 0), 5)
  
  def key_input(self, key):
    if self.visible and self.possibilityKeyPress:
      if key[pygame.K_a] == True or key[pygame.K_1] == True:
        self.x_slope = 0
      if key[pygame.K_s] == True or key[pygame.K_2] == True:
        self.x_slope = 1
      if key[pygame.K_d] == True or key[pygame.K_3] == True:
        self.x_slope = 2
      if key[pygame.K_f] == True or key[pygame.K_4] == True:
        self.x_slope = 3
      if key[pygame.K_g] == True or key[pygame.K_5] == True:
        self.x_slope = 4
      if key[pygame.K_h] == True or key[pygame.K_6] == True:
        self.x_slope = 5
      if key[pygame.K_j] == True or key[pygame.K_7] == True:
        self.x_slope = 6
      
      if key[pygame.K_LEFT] == True and self.x_slope > 0:
        self.leftKeyDown = True
      if key[pygame.K_LEFT] == False and self.leftKeyDown == True:
        self.leftKeyDown = False
        self.x_slope -= 1

      if key[pygame.K_RIGHT] == True and self.x_slope < 6:
        self.rightKeyDown = True
      if key[pygame.K_RIGHT] == False and self.rightKeyDown == True:
        self.rightKeyDown = False
        self.x_slope += 1
      
      if key[pygame.K_RETURN] == True:
        self.enter_key_down = True
      if key[pygame.K_RETURN] == False and self.enter_key_down:
        self.enter_key_down = False
        self.gamedirector.onEndPlayerTurn(2)
