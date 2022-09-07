class GameObject:
  root = None
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.children = []

  def key_input(self, key):
    for child in self.children:
      child.key_input(key)

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
