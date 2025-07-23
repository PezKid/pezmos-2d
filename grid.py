import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_axes(screen, origin, color, width):
  # get origin values
  Ox, Oy = origin
  
  # horizontal
  pygame.draw.line(screen, color, origin, (SCREEN_WIDTH, Oy), width=width)
  pygame.draw.line(screen, color, origin, (0, Oy), width=width)
  
  # vertical
  pygame.draw.line(screen, color, origin, (Ox, SCREEN_HEIGHT), width=width)
  pygame.draw.line(screen, color, origin, (Ox, 0), width=width)
  
def draw_grid(screen, origin, color, grid_size, width):
  # get origin values
  Ox, Oy = origin
  
  # horizontal
  for yadj in np.arange(0, SCREEN_HEIGHT - Oy, grid_size):
    posy, negy = Oy + yadj, Ox - yadj
    pygame.draw.line(screen, color, (0, posy), (SCREEN_WIDTH, posy), width=width)
    pygame.draw.line(screen, color, (0, negy), (SCREEN_WIDTH, negy), width=width)
  
  # vertical
  for xadj in np.arange(0, SCREEN_WIDTH - Ox, grid_size):
    posx, negx = Ox + xadj, Ox - xadj
    pygame.draw.line(screen, color, (posx, 0), (posx, SCREEN_WIDTH), width=width)
    pygame.draw.line(screen, color, (negx, 0), (negx, SCREEN_WIDTH), width=width)