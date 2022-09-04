import pygame
import sys

from gameobject import *
from player import *


tmr = 0
index = 0

def main():
  global tmr, index

  pygame.init()
  pygame.display.set_caption("4 Bingo!")
  screen = pygame.display.set_mode((670, 925))
  clock = pygame.time.Clock()

  root = GameObject()
  root.children.append(Player(75, 75, (255, 255, 255), 5))

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

    if index == 0:
      index = 1

    if index == 1:
      DrawRect(screen, 335, 637.5, 7, 6, 100, 100, 5)
      DrawText(screen, 335, 100, "4 Bingo!", 150, (255, 255, 255))

      DrawText(screen, 185, 200, "Player1 - 1:q 2:w 3:e 4:r 5:t 6:y 7:u", 30, (255, 255, 255))
      DrawText(screen, 182.5, 225, "Player2 - 1:a 2:s 3:d 4:f 5:g 6:h 7:j", 30, (255, 255, 255))
      DrawText(screen, 390, 212.5, "- >", 35, (255, 255, 255))
      DrawText(screen, 500, 212.5, "ENTER!", 50, (255, 255, 255))

      root.draw(screen)


    pygame.display.update()
    clock.tick(30)


def DrawRect(screen, x, y, row, column, width, height, thick):
  for i in range(row):
    for j in range(column):
      rx = (i*width - thick*i + x) - ((width*row - thick*(row - 1)) / 2)
      ry = (j*height - thick*j + y) - ((height*column - thick*(column - 1)) / 2)
      pygame.draw.rect(screen, (255, 255, 255), [rx, ry, width, height], thick)

def DrawText(screen, x, y, text, size, color):
  fnt = pygame.font.Font(None, size)
  sur = fnt.render(text, True, (color))
  screen.blit(sur, [x - sur.get_width() / 2, y - sur.get_height() / 2])


if __name__ == '__main__':
  main()
