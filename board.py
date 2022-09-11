from sqlite3 import Row
import pygame
from gameobject import *

class Board(GameObject):
  def __init__(self):
    super().__init__(335, 637.5, "Board")
    # 0:empty  1:player1  2:player2
    self.boardData = [
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
    ]
  
  def draw(self, screen):
    row = len(self.boardData)
    column = len(self.boardData[0])

    width = 100
    height = 100
    thick = 5

    for i in range(row):
      for j in range(column):
        rx = (j*width - thick*j + self.x) - ((width*column - thick*(column-1)) / 2)
        ry = (i*height - thick*i + self.y) - ((height*row - thick*(row-1)) / 2)
        pygame.draw.rect(screen, (255, 255, 255), [rx, ry, width, height], thick)

        if self.boardData[i][j] == 1:
          pygame.draw.circle(screen, (255, 0, 0), [rx+50, ry+50], 35, 5)
        elif self.boardData[i][j] == 2:
          pygame.draw.circle(screen, (0, 255, 0), [rx+50, ry+50], 35, 5)
        elif self.boardData[i][j] == 3:
          pygame.draw.circle(screen, (255, 0, 0), [rx+50, ry+50], 35, 35)
        elif self.boardData[i][j] == 4:
          pygame.draw.circle(screen, (0, 255, 0), [rx+50, ry+50], 35, 35)

  def setPosition(self, row, column, playerNum):
    self.boardData[row][column] = playerNum
