from player1 import *
from gameobject import *

class GameDirector(GameObject):
  def __init__(self, background, player1, player2):
    super().__init__(0, 0)
    self.background = background
    self.board = background.getBoard()
    self.timer = background.getTimer()
    self.player1 = player1
    self.player2 = player2

    # 0:StartScene / 1:Player1 / 2:Player2 / 3:Player1 Down / 4:Player2 Down / 5:EndScene(RedWin) / 6:EndScene(BlueWin) / 7:EndScene(Draw)
    self.mode = 0
    # 1:Player1 / 2:Player2
    self.turn = 1

    self.haveTime = True
    self.resetSecond = False
    self.toBeFilledStone = []
    self.toBeFilledStoneCheck = []
    self.press = False
    self.tmr = 0

    self.blop_sound = pygame.mixer.Sound("_sounds/MP_Blop.wav")
    self.tada_sound = pygame.mixer.Sound("_sounds/MP_Ta-Da.wav")
    self.button_sound = pygame.mixer.Sound("_sounds/MP_Tiny-Button-Push.wav")


  def key_input(self, key):
    if self.mode == 0 or (self.mode >= 5 and self.mode <= 7):
      if key[pygame.K_SPACE] == True:
        self.press = True
      if key[pygame.K_SPACE] == False and self.press == True:
        self.press = False
        self.button_sound.play()
        self.reset()


  def draw(self, screen):
    self.background.setMode(self.mode)
    self.timer.setMode(self.mode)

    if self.timer.second == 0:
      self.haveTime = False
      if self.mode == 1:
        self.mode = 3
      if self.mode == 2:
        self.mode = 4

    self.tmr = self.tmr + 1

    if self.mode == 1:
      self.player1.possibilityKeyPress = True
    if self.mode == 2:
      self.player2.possibilityKeyPress = True

    if self.mode == 3 and self.tmr % 2 == 0:
      board_x = self.player1.getColumnInBoard()
      board_y = self.player1.getRowInBoard()

      if board_y < 5 and self.board.boardData[0][board_x] != 0 and self.haveTime == False:
        self.mode = 6
        self.tada_sound.play()

      elif board_y < 5 and self.board.boardData[board_y+1][board_x] == 0:
          self.player1.moveToBoardY(board_y+1)
          if board_y == -1:
            self.resetSecond = True
      else:
        if board_y != -1:
          self.board.boardData[board_y][board_x] = 1
          if self.checkBingo(1, board_y, board_x):
            self.mode = 5
            self.tada_sound.play()

            for i in range(len(self.toBeFilledStone)):
              row, column = self.toBeFilledStone[i]
              self.board.boardData[row][column] = 3

          elif self.checkDraw():
            self.mode = 7
            self.tada_sound.play()

          else:
            self.changeToMode2()
            self.toBeFilledStoneCheck.clear()
        else:
          self.mode = 1

        if self.resetSecond == True:
          self.resetSecond = False
          self.timer.second = 20
    
    if self.mode == 4 and self.tmr % 2 == 0:
      board_x = self.player2.getColumnInBoard()
      board_y = self.player2.getRowInBoard()

      if board_y < 5 and self.board.boardData[0][board_x] != 0 and self.haveTime == False:
        self.mode = 5
        self.tada_sound.play()

      elif board_y < 5 and self.board.boardData[board_y+1][board_x] == 0:
        self.player2.moveToBoardY(board_y+1)
        if board_y == -1:
          self.resetSecond = True
      else:
        if board_y != -1:
          self.board.boardData[board_y][board_x] = 2
          if self.checkBingo(2, board_y, board_x):
            self.mode = 6
            self.tada_sound.play()

            for i in range(len(self.toBeFilledStone)):
              row, column = self.toBeFilledStone[i]
              self.board.boardData[row][column] = 4

          elif self.checkDraw():
            self.mode = 7
            self.tada_sound.play()
            
          else:
            self.changeToMode1()
            self.toBeFilledStoneCheck.clear()
        else:
          self.mode = 2
        
        if self.resetSecond == True:
          self.resetSecond = False
          self.timer.second = 20
    
    if self.mode >= 5 and self.mode <= 7:
      self.player1.setVisible(False)
      self.player2.setVisible(False)

  
  def onEndPlayerTurn(self, playerNum):
    if playerNum == 1:
      self.mode = 3
      self.player1.possibilityKeyPress = False
      self.blop_sound.play()

    if playerNum == 2:
      self.mode = 4
      self.player2.possibilityKeyPress = False
      self.blop_sound.play()


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
  

  def CountStoneUpDown(self, playerNum, row, column):
    sum = 0

    for i in range(row, -1, -1):
      if self.board.boardData[i][column] == playerNum:
        sum = sum + 1
        self.SetRowColumn(i, column)
      else: break
    for i in range(row+1, 6, 1):
      if self.board.boardData[i][column] == playerNum:
        sum = sum + 1
        self.SetRowColumn(i, column)
      else: break
    
    if sum == 4:
      self.appendToBeFilledStone()

    return sum

  def CountStoneLeftRight(self, playerNum, row, column):
    sum = 0

    for i in range(column, -1, -1):
      if self.board.boardData[row][i] == playerNum:
        sum = sum + 1
        self.SetRowColumn(row, i)
      else: break
    for i in range(column+1, 7, 1):
      if self.board.boardData[row][i] == playerNum:
        sum = sum + 1
        self.SetRowColumn(row, i)
      else: break

    if sum == 4:
      self.appendToBeFilledStone()
    
    return sum
  
  def CountStoneDiagonal1(self, playerNum, row, column):
    sum = 0

    for i in range(7):
      if row-i == -1 or column-i == -1: break
      else:
        if self.board.boardData[row-i][column-i] == playerNum:
          sum = sum + 1
          self.SetRowColumn(row-i, column-i)
        else: break
    for i in range(1, 7):
      if row+i == 6 or column+i == 7: break
      else:
        if self.board.boardData[row+i][column+i] == playerNum:
          sum = sum + 1
          self.SetRowColumn(row+i, column+i)
        else: break

    if sum == 4:
      self.appendToBeFilledStone()
    
    return sum
  
  def CountStoneDiagonal2(self, playerNum, row, column):
    sum = 0

    for i in range(7):
      if row-i == -1 or column+i == 7: break
      else:
        if self.board.boardData[row-i][column+i] == playerNum:
          sum = sum + 1
          self.SetRowColumn(row-i, column+i)
        else: break
    for i in range(1, 7):
      if row+i == 6 or column-i == -1: break
      else:
        if self.board.boardData[row+i][column-i] == playerNum:
          sum = sum + 1
          self.SetRowColumn(row+i, column-i)
        else: break

    if sum == 4:
      self.appendToBeFilledStone()
    
    return sum
  
  def CountAllStone(self):
    sum = 0

    for i in range(7):
      for j in range(6):
        if self.board.boardData[j][i] == 1 or self.board.boardData[j][i] == 2:
          sum = sum + 1
    
    return sum


  def checkBingo(self, playerNum, row, column):
    bingoCount = 0

    self.toBeFilledStoneCheck.clear()
    if self.CountStoneUpDown(playerNum, row, column) == 4:
      bingoCount += 1
    self.toBeFilledStoneCheck.clear()
    if self.CountStoneLeftRight(playerNum, row, column) == 4:
      bingoCount += 1
    self.toBeFilledStoneCheck.clear()
    if self.CountStoneDiagonal1(playerNum, row, column) == 4:
      bingoCount += 1
    self.toBeFilledStoneCheck.clear()
    if self.CountStoneDiagonal2(playerNum, row, column) == 4:
      bingoCount += 1
    self.toBeFilledStoneCheck.clear()

    if bingoCount > 0:
      return True
    else:
      return False

  def checkDraw(self):
    if self.CountAllStone() == 42:
      return True
    else:
      return False
  

  def SetRowColumn(self, row, column):
    if len(self.toBeFilledStoneCheck) == 0:
      self.toBeFilledStoneCheck.append((row, column))
    else:
      # for i in range(len(self.toBeFilledStoneCheck)):
      x, y = self.toBeFilledStoneCheck[len(self.toBeFilledStoneCheck)-1]
      if x != row or y != column:
        self.toBeFilledStoneCheck.append((row, column))
  
  def appendToBeFilledStone(self):
    for i in range(4):
      row, column = self.toBeFilledStoneCheck[i]
      self.toBeFilledStone.append((row, column))
    self.toBeFilledStoneCheck.clear()


  def reset(self):
    self.tmr = 0
    self.turn = (self.turn + 1) % 2
    self.mode = self.turn + 1
    self.haveTime = True
    self.resetSecond = False

    if self.mode == 1:
      self.player1.setVisible(True)
      self.player2.setVisible(False)
    if self.mode == 2:
      self.player2.setVisible(True)
      self.player1.setVisible(False)
    
    self.toBeFilledStone.clear()
    self.toBeFilledStoneCheck.clear()

    self.player1.reset()
    self.player2.reset()
    self.board.boardData = [
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
    ]
