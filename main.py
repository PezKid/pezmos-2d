import pygame
import math
import numpy as np

# colors
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (100, 100, 100)
AXES_COLOR = (0, 0, 0)

SCREEN_DIMS = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
GRID_SIZE = 20
AXES_WIDTH = 3
GRID_WIDTH = 1
ORIGIN = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

screen = pygame.display.set_mode(SCREEN_DIMS)

def draw_axes(origin, color, width):
  # get origin values
  Ox, Oy = origin
  
  # horizontal
  pygame.draw.line(screen, color, origin, (SCREEN_WIDTH, Oy), width=width)
  pygame.draw.line(screen, color, origin, (0, Oy), width=width)
  
  # vertical
  pygame.draw.line(screen, color, origin, (Ox, SCREEN_HEIGHT), width=width)
  pygame.draw.line(screen, color, origin, (Ox, 0), width=width)
  
def draw_grid(origin, color, grid_size, width):
  # get origin values
  Ox, Oy = origin
  
  # horizontal
  for yadj in np.arange(0, SCREEN_HEIGHT - Oy, grid_size):
    posy, negy = Oy + yadj, Ox - yadj
    pygame.draw.line(screen, color, (0, posy), (SCREEN_WIDTH, posy), width=width)
    pygame.draw.line(screen, color, (0, negy), (SCREEN_WIDTH, negy), width=width)
  
  # vertical Q1, Q2
  for xadj in np.arange(0, SCREEN_WIDTH - Ox, grid_size):
    posx, negx = Ox + xadj, Ox - xadj
    pygame.draw.line(screen, color, (posx, 0), (posx, SCREEN_WIDTH), width=width)
    pygame.draw.line(screen, color, (negx, 0), (negx, SCREEN_WIDTH), width=width)

running = True
while (running):
  
  key = pygame.key.get_pressed()
  if (key[pygame.K_UP]):
    GRID_SIZE = GRID_SIZE + 0.05
  elif (key[pygame.K_DOWN]):
    GRID_SIZE = GRID_SIZE - 0.05
  
  screen.fill(BACKGROUND_COLOR)
  draw_grid(ORIGIN, GRID_COLOR, GRID_SIZE, GRID_WIDTH)
  draw_axes(ORIGIN, AXES_COLOR, AXES_WIDTH)
  
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
  
  pygame.display.flip()

pygame.quit()