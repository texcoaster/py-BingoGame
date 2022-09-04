import pygame
from gameobject import *

class Player(GameObject):
  def __init__(self, width, height, color, thick):
    super().__init__()
    self.width = width
    self.height = height
    self.color = color
    self.thick = thick
  
  def draw(self, screen):
    print("player")
    pass
