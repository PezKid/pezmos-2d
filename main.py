import pygame
from config import *
from coords import *
from grid import draw_axes, draw_grid
from functions import *
from input import mouse_click

# setup pygame
screen = pygame.display.set_mode(SCREEN_DIMS)
pygame.display.set_caption("Pezmos")
clock = pygame.time.Clock()

# initialize variables
grid_size = GRID_SIZE_DEFAULT
running = True

def draw_function(f, color, width=3):
  prev = None
  for pyx in range(0, SCREEN_WIDTH):
    x, _ = global_to_grid_coords((pyx, 0), grid_size=grid_size)
    y = f(x)
    output = grid_to_global_coords((x, y), grid_size=grid_size)
    
    if prev is not None:
      pygame.draw.line(screen, color, prev, output, width)
    
    prev = output

# main game loop
while (running):
  
  # set framerate
  clock.tick(FPS_LIMIT)
  
  # handles input that scales the grid size, up arrow to zoom in, down arrow to zoom out
  key = pygame.key.get_pressed()
  if (key[pygame.K_UP]):
    grid_size = grid_size * 1.05
    if (grid_size > 100):
      grid_size = 100
  elif (key[pygame.K_DOWN]):
    grid_size = grid_size * 0.95
    if (grid_size < 3):
      grid_size = 3
  
  # draw background and grid
  screen.fill(BACKGROUND_COLOR)
  draw_grid(screen, ORIGIN, GRID_COLOR, grid_size, GRID_WIDTH)
  draw_axes(screen, ORIGIN, AXES_COLOR, AXES_WIDTH)
  
  draw_function(f1, RED)
  draw_function(f2, GREEN)
  draw_function(f3, BLUE)
  
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