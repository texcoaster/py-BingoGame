import pygame
import sys

from gameobject import *
from background import *
from playerdirector import *
from player1 import *



tmr = 0
index = 0

press = False

def main():
  global tmr, index, press

  pygame.init()
  pygame.display.set_caption("4 Bingo!")
  screen = pygame.display.set_mode((670, 925))
  clock = pygame.time.Clock()

  root = GameObject(0, 0)
  GameObject.root = root
  background = BackGround()
  root.children.append(background)
  root.children.append(PlayerDirector())

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

    root.draw(screen)
    root.key_input(key)

    background.SetIndex(index)

    if index == 0:
      if key[pygame.K_SPACE] == True:
        press = True
      if key[pygame.K_SPACE] == False and press == True:
        index = 1
        press = False
        PlayerDirector.pl_flag = True

    if index == 1:
      ...
    
    if index == 2:
      ...

    pygame.display.update()
    clock.tick(30)


if __name__ == '__main__':
  main()
