import pygame
from gameobject import *

class Timer(GameObject):
  def __init__(self):
    super().__init__(620, 180)
    self.reset()
  
  def draw(self, screen):
    if self.mode > 0 and self.mode < 5:
      self.drawText(screen, self.x, self.y, str("%.1f" %self.second), 60, self.color)

      if self.mode > 0 and self.mode < 3:
        self.tmr += 1
        self.checkSecond()
        self.changeColor()
      else:
        self.tmr = 0
    else:
      self.reset()

  def setMode(self, mode):
    self.mode = mode

  def reset(self):
    self.second = 20.0
    self.tmr = 0
    self.color = (255, 255, 255)
    self.mode = 0

  def drawText(self, screen, x, y, text, size, color):
    fnt = pygame.font.Font(None, size)
    sur = fnt.render(text, True, (color))
    screen.blit(sur, [x - sur.get_width() / 2, y - sur.get_height() / 2])

  def checkSecond(self):
    if self.second > 0.1:
      if self.tmr % 3 == 0:
        self.second -= 0.1
    else:
      self.second = 0.0

  def changeColor(self):
    if self.second > 7:
      self.color = (255, 255, 255)
    elif self.second > 3:
      self.color = (255, 228, 0)
    else:
      self.color = (255, 0, 0)
