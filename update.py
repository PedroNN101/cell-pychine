from grid import grid, setCell;from define_types import Cell
def update(steps:int,grid:list):
    auxgrid = grid
    for _ in range(steps):
        for row in grid:
            for cell in row:
                if cell["name"] == "mover":
                    grid[auxgrid.index(row)][auxgrid[grid.index(row)]]
