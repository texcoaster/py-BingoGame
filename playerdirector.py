from player import *
from gameobject import *

class PlayerDirector(GameObject):
  def __init__(self):
    super().__init__()
    self.pl_x = [47.85, 143.55, 239.25, 334.95, 430.65, 526.35, 622.05]

  def draw(self, screen):
    self.children.append(Player(self.pl_x[6], 300, 35, (255, 255, 255), 5))

    for child in self.children:
      GameObject.root.children.append(child)
