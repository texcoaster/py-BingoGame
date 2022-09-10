import pygame
from gameobject import *

class BasePlayer(GameObject):
  def __init__(self, name, x, y, radius, color, thick):
    super().__init__(x, y, name)
    self.reset()

    self.radius = radius
    self.speed = 95

    self.color = color
    self.thick = thick

    self.possibilityKeyPress = False
    self.enter_key_down = False
    self.leftKeyDown = False
    self.rightKeyDown = False

    self.visible = False
    self.gamedirector = None

  def draw(self, screen):
    if self.visible == True:
      pygame.draw.circle(screen, self.color, [50 + 95 * self.x_slope, 400 + 95 * self.y_slope], self.radius, self.thick)

  def setVisible(self, visible):
    self.visible = visible

  def setGameDirector(self, gamedirector):
    self.gamedirector = gamedirector
  
  def getColumnInBoard(self):
    return self.x_slope
  
  def getRowInBoard(self):
    return self.y_slope
  
  def moveToBoardY(self, board_y):
    self.y_slope = board_y
  
  def reset(self):
    self.x_slope = 0
    self.y_slope = -1
