import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coords import global_to_grid_coords, grid_to_global_coords

# test to make sure global2grid and grid2global are inverses
def test_conversion_roundtrip():
    original = (200, 300)
    grid_coords = global_to_grid_coords(original)
    back = grid_to_global_coords(grid_coords)
    assert abs(original[0] - back[0]) < 1e-6
    assert abs(original[1] - back[1]) < 1e-6