from player1 import *
from gameobject import *

class PlayerDirector(GameObject):
  pl_flag = False
  def __init__(self):
    super().__init__(0, 0)
    self.pl_type = 0

  def draw(self, screen):
    if PlayerDirector.pl_flag:
      self.children.append(Player1(47.85, 300, 35, (255, 255, 255), 5, self.pl_type))
      PlayerDirector.pl_flag = False
      self.pl_type = (self.pl_type + 1) % 2

    for child in self.children:
      GameObject.root.children.append(child)
