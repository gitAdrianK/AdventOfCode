from enum import IntFlag

class Cardinal(IntFlag):
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270

class Sagittal(IntFlag):
    LEFT = -1
    RIGHT = 1

class Ferry:
    def __init__(self) -> None:
        self.pos_x = 0
        self.pos_y = 0
        self.facing = Cardinal.EAST

    def move(self, cardinal, amount):
        if cardinal is Cardinal.NORTH:
            self.pos_y += amount
        elif cardinal is Cardinal.EAST:
            self.pos_x += amount
        elif cardinal is Cardinal.SOUTH:
            self.pos_y -= amount
        elif cardinal is Cardinal.WEST:
            self.pos_x -= amount

    def turn(self, sagittal, amount):
        amount *= sagittal
        self.facing = Cardinal((self.facing + amount) % 360)

def solveDay12(input):
    # Setup
    ferry = Ferry()
    f = open(input, "r")
    for line in f.readlines():
        var = line[0]
        if var == "L":
            ferry.turn(Sagittal.LEFT, int(line[1:]))
        elif var == "R":
            ferry.turn(Sagittal.RIGHT, int(line[1:]))
        elif var == "N":
            ferry.move(Cardinal.NORTH, int(line[1:]))
        elif var == "E":
            ferry.move(Cardinal.EAST, int(line[1:]))
        elif var == "S":
            ferry.move(Cardinal.SOUTH, int(line[1:]))
        elif var == "W":
            ferry.move(Cardinal.WEST, int(line[1:]))
        elif var == "F":
            ferry.move(ferry.facing, int(line[1:]))
    # Part 1
    p1 = abs(ferry.pos_x) + abs(ferry.pos_y)
    return (p1, 0)


assert((25, 0) == solveDay12("test_input.txt"))
print(solveDay12("input.txt"))
