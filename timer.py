import pygame
from gameobject import *

class Timer(GameObject):
  def __init__(self):
    super().__init__(620, 180)
    self.second = 20
    self.tmr = 0

    self.color = (0, 0, 255)
    self.mode = 0
  
  def draw(self, screen):
    if self.mode == 1:
      self.tmr += 1

      self.checkSecond(self.second)
      self.changeColor(self.tmr)

      fnt = pygame.font.Font(None, 60)
      sur = fnt.render(str(self.second), True, self.color)
      screen.blit(sur, [self.x - sur.get_width() / 2, self.y - sur.get_height() / 2])

  def setMode(self, mode):
    self.mode = mode
  
  def checkSecond(self, second):
    if self.second > 0:
      if self.tmr % 30 == 0:
        self.second -= 1
    else:
      self.second = 20
  
  def changeColor(self, tmr):
    if self.second > 7:
      self.color = (255, 255, 255)
    elif self.second > 3:
      self.color = (255, 228, 0)
    else:
      self.color = (255, 0, 0)
