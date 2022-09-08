import define_types;from pygame import Vector2
grid = None
def setCell(type:str,x:int,y:int,rotation:int):
    cell = define_types.Cell(type, rotation,Vector2(x,y))
    grid[y-1][x-1] = cell.data