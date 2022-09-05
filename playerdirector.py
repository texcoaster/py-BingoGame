from player import *
from gameobject import *

class PlayerDirector(GameObject):
  def __init__(self):
    super().__init__()

  def draw(self, screen):
    self.children.append(Player(47.85, 300, 35, (255, 255, 255), 5))

    for child in self.children:
      GameObject.root.children.append(child)
