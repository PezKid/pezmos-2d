from coords import global_to_grid_coords

# prints grid coordinates user clicked from event
def mouse_click(event, grid_size):
    mouse_x, mouse_y = global_to_grid_coords(event.pos, grid_size=grid_size)
    print(f"({mouse_x:.2f}, {mouse_y:.2f}) click detected")