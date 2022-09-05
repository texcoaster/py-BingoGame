class GameObject:
  root = None
  def __init__(self):
    self.x = 0
    self.y = 0
    self.children = []

  def key_input(self, key):
    for child in self.children:
      child.key_input(key)

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
