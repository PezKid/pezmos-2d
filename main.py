import pygame
from config import *
from coords import *
from grid import draw_axes, draw_grid
from input import mouse_click

# setup pygame
screen = pygame.display.set_mode(SCREEN_DIMS)
pygame.display.set_caption("Pezmos")
clock = pygame.time.Clock()

# initialize variables
grid_size = GRID_SIZE_DEFAULT
running = True

# main game loop
while (running):
  
  # set framerate
  clock.tick(FPS_LIMIT)
  
  # handles input that scales the grid size, up arrow to zoom in, down arrow to zoom out
  key = pygame.key.get_pressed()
  if (key[pygame.K_UP]):
    grid_size = grid_size + 1
  elif (key[pygame.K_DOWN]):
    grid_size = grid_size - 1
  
  # draw background and grid
  screen.fill(BACKGROUND_COLOR)
  draw_grid(screen, ORIGIN, GRID_COLOR, grid_size, GRID_WIDTH)
  draw_axes(screen, ORIGIN, AXES_COLOR, AXES_WIDTH)
  
  # event loop
  for event in pygame.event.get():
    # quits game
    if (event.type == pygame.QUIT): 
      running = False
    # prints grid coordinate on click, used to debug coordinate system
    elif (event.type == pygame.MOUSEBUTTONDOWN):
      mouse_click(event, grid_size)
  
  # update screen
  pygame.display.flip()

# end application
pygame.quit()