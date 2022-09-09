import pygame
from gameobject import *

class Player1(GameObject):
  def __init__(self, x, y, radius, color, thick, mode):
    super().__init__(x, y)
    self.radius = radius
    self.speed = 100

    self.color = color
    self.thick = thick
    self.mode = mode

    self.press = False
    self.tmr = 0
    self.pl_x = [47.85, 143.55, 239.25, 334.95, 430.65, 526.35, 622.05]
  
  def key_input(self, key):
    if self.mode == 0:
      if key[pygame.K_q] == True:
        self.x = self.pl_x[0]
      if key[pygame.K_w] == True:
        self.x = self.pl_x[1]
      if key[pygame.K_e] == True:
        self.x = self.pl_x[2]
      if key[pygame.K_r] == True:
        self.x = self.pl_x[3]
      if key[pygame.K_t] == True:
        self.x = self.pl_x[4]
      if key[pygame.K_y] == True:
        self.x = self.pl_x[5]
      if key[pygame.K_u] == True:
        self.x = self.pl_x[6]
      
      if key[pygame.K_RETURN] == True:
        self.press = True
      if key[pygame.K_RETURN] == False and self.press:
        self.mode = 1

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius, self.thick)

    if self.mode == 1:
      self.tmr = self.tmr + 1
      print(self.tmr % 30)

      if self.tmr % 180 == 0:
        self.y = self.y + self.speed
        if self.y > 910:
          self.mode = 2
