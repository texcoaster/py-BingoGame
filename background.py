import pygame
from gameobject import *
from board import *

class BackGround(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.tmr = 0
    self.mode = 0

    self.children.append(Board())
  
  def draw(self, screen):
    screen.fill((0, 0, 0))

    if self.mode == 0:
      self.tmr += 1

      self.DrawText(screen, 335, 100, "4 Bingo!", 150, (255, 255, 255))
      if self.tmr % 30 > 15:
        self.DrawText(screen, 335, 250, "press space to start", 50, (255, 255, 255))

    if self.mode == 1:
      self.DrawText(screen, 335, 100, "4 Bingo!", 150, (255, 255, 255))

      self.DrawText(screen, 185, 200, "Player1 - 1:q 2:w 3:e 4:r 5:t 6:y 7:u", 30, (255, 255, 255))
      self.DrawText(screen, 182.5, 225, "Player2 - 1:a 2:s 3:d 4:f 5:g 6:h 7:j", 30, (255, 255, 255))
      self.DrawText(screen, 390, 212.5, "- >", 35, (255, 255, 255))
      self.DrawText(screen, 500, 212.5, "ENTER!", 50, (255, 255, 255))
    
    if self.mode == 2:
      self.tmr = 0
    
    super().draw(screen)

  def SetMode(self, mode):
    self.mode = mode

  def DrawText(self, screen, x, y, text, size, color):
    fnt = pygame.font.Font(None, size)
    sur = fnt.render(text, True, (color))
    screen.blit(sur, [x - sur.get_width() / 2, y - sur.get_height() / 2])
