import numpy as np
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
    def __init__(self):
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

    def move_by_waypoint(self, waypoint):
        self.pos_x += waypoint.pos_x
        self.pos_y += waypoint.pos_y

    def rotate(self, sagittal, amount):
        amount *= sagittal
        self.facing = Cardinal((self.facing + amount) % 360)


class Waypoint:
    def __init__(self):
        self.pos_x = 10
        self.pos_y = 1

    def move(self, cardinal, amount):
        if cardinal is Cardinal.NORTH:
            self.pos_y += amount
        elif cardinal is Cardinal.EAST:
            self.pos_x += amount
        elif cardinal is Cardinal.SOUTH:
            self.pos_y -= amount
        elif cardinal is Cardinal.WEST:
            self.pos_x -= amount

    def rotate(self, sagittal, amount):
        if sagittal is Sagittal.RIGHT:
            amount *= -1
        theta = np.radians(amount)
        c, s = int(np.cos(theta)), int(np.sin(theta))
        rot_matrix = np.array(((c, -s), (s, c)))
        pos_vec = np.array((self.pos_x, self.pos_y))
        result = np.matmul(rot_matrix, pos_vec)
        self.pos_x, self.pos_y = result[0], result[1]


def solveDay12(input):
    # Setup
    ferry = Ferry()
    f = open(input, "r")
    lines = list(l for l in f.readlines())
    # Part 1
    for line in lines:
        var = line[0]
        if var == "L":
            ferry.rotate(Sagittal.LEFT, int(line[1:]))
        elif var == "R":
            ferry.rotate(Sagittal.RIGHT, int(line[1:]))
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
    p1 = abs(ferry.pos_x) + abs(ferry.pos_y)
    # Part 2
    ferry = Ferry()
    waypoint = Waypoint()
    for line in lines:
        var = line[0]
        if var == "L":
            waypoint.rotate(Sagittal.LEFT, int(line[1:]))
        elif var == "R":
            waypoint.rotate(Sagittal.RIGHT, int(line[1:]))
        elif var == "N":
            waypoint.move(Cardinal.NORTH, int(line[1:]))
        elif var == "E":
            waypoint.move(Cardinal.EAST, int(line[1:]))
        elif var == "S":
            waypoint.move(Cardinal.SOUTH, int(line[1:]))
        elif var == "W":
            waypoint.move(Cardinal.WEST, int(line[1:]))
        elif var == "F":
            for i in range(int(line[1:])):
                ferry.move_by_waypoint(waypoint)
    p2 = abs(ferry.pos_x) + abs(ferry.pos_y)
    return (p1, p2)


assert((25, 286) == solveDay12("test_input.txt"))
print(solveDay12("input.txt"))
