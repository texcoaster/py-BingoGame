import pygame

class Player():
  def __init__(self, x, y, radius, color, thick):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.thick = thick
  
  def draw(self, screen):
    pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius, self.thick)
