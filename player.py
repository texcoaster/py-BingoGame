import pygame

class Player():
  def __init__(self, x, y, radius, color, thick):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.thick = thick
    self.pl_x = [47.85, 143.55, 239.25, 334.95, 430.65, 526.35, 622.05]
  
  def key_input(self, key):
    if key[pygame.K_q] == True or key[pygame.K_a] == True:
      self.x = self.pl_x[0]
    if key[pygame.K_w] == True or key[pygame.K_s] == True:
      self.x = self.pl_x[1]
    if key[pygame.K_e] == True or key[pygame.K_d] == True:
      self.x = self.pl_x[2]
    if key[pygame.K_r] == True or key[pygame.K_f] == True:
      self.x = self.pl_x[3]
    if key[pygame.K_t] == True or key[pygame.K_g] == True:
      self.x = self.pl_x[4]
    if key[pygame.K_y] == True or key[pygame.K_h] == True:
      self.x = self.pl_x[5]
    if key[pygame.K_u] == True or key[pygame.K_j] == True:
      self.x = self.pl_x[6]

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius, self.thick)
