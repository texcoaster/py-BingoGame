import pygame
from gameobject import *

class Player1(GameObject):
  def __init__(self, x, y, radius, color, thick):
    super().__init__(x, y, "Player1")
    self.radius = radius
    self.speed = 95

    self.color = color
    self.thick = thick
    self.mode = 0

    self.press = False
    self.visible = False
    self.tmr = 0
    self.pl_x = [50, 145, 240, 335, 430, 525, 620]
  
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

      if self.tmr % 15 == 0:
        self.y = self.y + self.speed
        if self.y > 600:
          self.mode = 2
  
  def SetVisible(self, visible):
    self.visible = visible
