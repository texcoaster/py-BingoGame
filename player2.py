import pygame
from gameobject import *

class Player2(GameObject):
  def __init__(self, x, y, radius, color, thick):
    super().__init__(x, y, "Player2")
