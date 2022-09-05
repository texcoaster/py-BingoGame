import pygame
from gameobject import *

class BackGround(GameObject):
  def __init__(self):
    self.tmr = 0
  
  def draw(self, screen, index):
    screen.fill((0, 0, 0))

    if index == 0:
      self.tmr += 1

      self.DrawRect(screen, 335, 637.5, 7, 6, 100, 100, 5)
      self.DrawText(screen, 335, 100, "4 Bingo!", 150, (255, 255, 255))
      if self.tmr % 30 > 15:
        self.DrawText(screen, 335, 250, "press space to start", 50, (255, 255, 255))

    if index == 1:
      self.DrawRect(screen, 335, 637.5, 7, 6, 100, 100, 5)
      self.DrawText(screen, 335, 100, "4 Bingo!", 150, (255, 255, 255))

      self.DrawText(screen, 185, 200, "Player1 - 1:q 2:w 3:e 4:r 5:t 6:y 7:u", 30, (255, 255, 255))
      self.DrawText(screen, 182.5, 225, "Player2 - 1:a 2:s 3:d 4:f 5:g 6:h 7:j", 30, (255, 255, 255))
      self.DrawText(screen, 390, 212.5, "- >", 35, (255, 255, 255))
      self.DrawText(screen, 500, 212.5, "ENTER!", 50, (255, 255, 255))
    
    if index == 2:
      self.tmr = 0
  
  def DrawRect(self, screen, x, y, row, column, width, height, thick):
    for i in range(row):
      for j in range(column):
        rx = (i*width - thick*i + x) - ((width*row - thick*(row - 1)) / 2)
        ry = (j*height - thick*j + y) - ((height*column - thick*(column - 1)) / 2)
        pygame.draw.rect(screen, (255, 255, 255), [rx, ry, width, height], thick)

  def DrawText(self, screen, x, y, text, size, color):
    fnt = pygame.font.Font(None, size)
    sur = fnt.render(text, True, (color))
    screen.blit(sur, [x - sur.get_width() / 2, y - sur.get_height() / 2])
