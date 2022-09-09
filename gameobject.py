class GameObject:
  root = None
  def __init__(self, x, y, name=None):
    self.x = x
    self.y = y
    self.children = []
    self.name = name

  def key_input(self, key):
    for child in self.children:
      child.key_input(key)

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
