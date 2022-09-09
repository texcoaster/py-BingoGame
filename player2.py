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
    self.down = False
    self.tmr = 0
    self.pl_x = [47.85, 143.55, 239.25, 334.95, 430.65, 526.35, 622.05]
  
  def key_input(self, key):
    if (key[pygame.K_q] == True and self.mode == 0) or (key[pygame.K_a] == True and self.mode == 1):
      self.x = self.pl_x[0]
    if (key[pygame.K_w] == True and self.mode == 0) or (key[pygame.K_s] == True and self.mode == 1):
      self.x = self.pl_x[1]
    if (key[pygame.K_e] == True and self.mode == 0) or (key[pygame.K_d] == True and self.mode == 1):
      self.x = self.pl_x[2]
    if (key[pygame.K_r] == True and self.mode == 0) or (key[pygame.K_f] == True and self.mode == 1):
      self.x = self.pl_x[3]
    if (key[pygame.K_t] == True and self.mode == 0) or (key[pygame.K_g] == True and self.mode == 1):
      self.x = self.pl_x[4]
    if (key[pygame.K_y] == True and self.mode == 0) or (key[pygame.K_h] == True and self.mode == 1):
      self.x = self.pl_x[5]
    if (key[pygame.K_u] == True and self.mode == 0) or (key[pygame.K_j] == True and self.mode == 1):
      self.x = self.pl_x[6]
    
    if key[pygame.K_RETURN] == True:
      self.press = True
    if key[pygame.K_RETURN] == False and self.press:
      self.down = True

  def draw(self, screen):
    tmr = tmr + 1
    pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius, self.thick)

    if self.down:
      self.y = self.y + self.speed
