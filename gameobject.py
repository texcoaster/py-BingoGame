class GameObject:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.children = []

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
