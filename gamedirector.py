from player1 import *
from gameobject import *

class GameDirector(GameObject):
  def __init__(self, background, player1, player2):
    super().__init__(0, 0)
    self.background = background
    self.player1 = player1
    self.player2 = player2

    self.mode = 0
    self.press = False

  def key_input(self, key):
    if self.mode == 0:
      if key[pygame.K_SPACE] == True:
        self.press = True
      if key[pygame.K_SPACE] == False and self.press == True:
        self.press = False
        self.mode = 1

  def draw(self, screen):
    self.background.SetMode(self.mode)
