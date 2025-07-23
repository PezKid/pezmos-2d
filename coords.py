from config import GRID_SIZE_DEFAULT, ORIGIN

# converts global pygame coordinates to grid coordinates. relies on origin location and grid_size
def global_to_grid_coords(coords, origin=ORIGIN, grid_size=GRID_SIZE_DEFAULT):
    x_coord, y_coord = coords
    Ox, Oy = origin
    return ((x_coord - Ox) / grid_size, -(y_coord - Oy) / grid_size)

# converts grid coordinates to global pygame coordinates. relies on origin location and grid_size
def grid_to_global_coords(coords, origin=ORIGIN, grid_size=GRID_SIZE_DEFAULT):
    x_coord, y_coord = coords
    Ox, Oy = origin
    return (grid_size * x_coord + Ox, -(grid_size * y_coord) + Oy)