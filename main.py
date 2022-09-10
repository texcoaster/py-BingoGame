import pygame
import sys

from gameobject import *
from background import *
from player1 import *
from player2 import *
from gamedirector import *


tmr = 0

def main():
  global tmr

  pygame.init()
  pygame.display.set_caption("4 Bingo!")
  screen = pygame.display.set_mode((670, 925))
  clock = pygame.time.Clock()


  root = GameObject(0, 0)
  GameObject.root = root

  background = BackGround()
  player1 = Player1()
  player2 = Player2()
  gamedirector = GameDirector(background, player1, player2)

  player1.setGameDirector(gamedirector)
  player2.setGameDirector(gamedirector)

  root.children.append(background)
  root.children.append(player1)
  root.children.append(player2)
  root.children.append(gamedirector)


  while True:
    tmr = tmr + 1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
          screen = pygame.display.set_mode((670, 925), pygame.FULLSCREEN)
        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
          screen = pygame.display.set_mode((670, 925))

    key = pygame.key.get_pressed()

    root.key_input(key)
    root.draw(screen)


    pygame.display.update()
    clock.tick(30)


if __name__ == '__main__':
  main()
