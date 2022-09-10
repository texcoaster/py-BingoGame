from player1 import *
from gameobject import *

class GameDirector(GameObject):
  def __init__(self, background, player1, player2):
    super().__init__(0, 0)
    self.background = background
    self.board = background.getBoard()
    self.player1 = player1
    self.player2 = player2

    # 0:StartScene / 1:Player1 / 2:Player2 / 3:Player1 Down / 4:Player2 Down / 5:EndScene
    self.mode = 0
    self.press = False
    self.tmr = 0

  def key_input(self, key):
    if self.mode == 0:
      if key[pygame.K_SPACE] == True:
        self.press = True
      if key[pygame.K_SPACE] == False and self.press == True:
        self.press = False
        self.mode = 1
        self.player1.setVisible(True)

  def draw(self, screen):
    self.background.setMode(self.mode)

    self.tmr = self.tmr + 1

    if self.mode == 3 and self.tmr % 5 == 0:
      board_x = self.player1.getColumnInBoard()
      board_y = self.player1.getRowInBoard()
      if board_y < 5 and self.board.boardData[board_y+1][board_x] == 0:
          self.player1.moveToBoardY(board_y+1)
      else:
        if board_y != -1:
          self.board.boardData[board_y][board_x] = 1
          self.changeToMode2()
        else:
          self.mode = 1
    
    if self.mode == 4 and self.tmr % 5 == 0:
      board_x = self.player2.getColumnInBoard()
      board_y = self.player2.getRowInBoard()
      if board_y < 5 and self.board.boardData[board_y+1][board_x] == 0:
        self.player2.moveToBoardY(board_y+1)
      else:
        if board_y != -1:
          self.board.boardData[board_y][board_x] = 2
          self.changeToMode1()
        else:
          self.mode = 2

  
  def onEndPlayerTurn(self, playerNum):
    if playerNum == 1:
      self.mode = 3
    if playerNum == 2:
      self.mode = 4

  def changeToMode1(self):
    self.mode = 1
    self.player2.setVisible(False)
    self.player1.setVisible(True)
    self.player2.reset()

  def changeToMode2(self):
    self.mode = 2
    self.player1.setVisible(False)
    self.player2.setVisible(True)
    self.player1.reset()
