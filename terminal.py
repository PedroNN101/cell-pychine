import grid;import update;import define_types;from pygame import Vector2
from numpy import zeros
def create_grid(width: int, height: int):
    return zeros((width, height), define_types.Cell)
def Loop():
    while True:
        cmd = input(">> ")
        if cmd.split()[0] == "create-grid":
            a = int(cmd.split()[1])
            b = int(cmd.split()[2])
            grid.grid = create_grid(a, b)
        elif cmd == "show-grid":
            print(grid.grid)
        elif cmd.split()[0] == "set-cell":
            a = cmd.split()[1]
            b = int(cmd.split()[2])
            c = int(cmd.split()[3])
            d = int(cmd.split()[4])
            grid.setCell(a, rotation=b, x=c, y=d)
        elif cmd == "rotation-help":
            print("0: Facing UP\n90: Facing RIGHT\n180: Facing DOWN\n-90: Facing LEFT")