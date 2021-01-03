from os import write
from intcode_computer import IntCodeComputer, Status
from enum import Enum, IntEnum
import re


class Facing(IntEnum):
    UP = 3
    LEFT = 2
    DOWN = 1
    RIGHT = 0


class Turn(Enum):
    LEFT = 0
    RIGHT = 1


class Robot:
    def __init__(self):
        self.facing = Facing.UP
        self.x = 0
        self.y = 0

    def turn(self, turn):
        if turn == 0:
            turn = -1
        self.facing = Facing(((self.facing + turn) % 4))

    def move(self):
        if self.facing == Facing.UP:
            self.y -= 1
        elif self.facing == Facing.LEFT:
            self.x -= 1
        elif self.facing == Facing.DOWN:
            self.y += 1
        elif self.facing == Facing.RIGHT:
            self.x += 1


def solve_day_11(input):
    # Instead of using a set for what panels have been painted
    # to see how many panels the robot paints at least once
    # I am just gonna gamble that part 2 asks about what was painted
    # so I can just go and print this dict
    panels = {}
    robot = Robot()
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    # computer.write(0) # Use this to start on a black panel for part 1
    computer.write(1)  # Use this to start on a white panel for part 2
    computer.run()
    output = computer.read()
    paint_as = output[0]
    turn = output[1]
    panels[(robot.x, robot.y)] = paint_as
    robot.turn(turn)
    robot.move()
    while computer.status != Status.TERMINATED:
        if (robot.x, robot.y) in panels:
            computer.write(panels[(robot.x, robot.y)])
        else:
            computer.write(0)
        computer.run()
        output = computer.read()
        paint_as = output[0]
        turn = output[1]
        panels[(robot.x, robot.y)] = paint_as
        robot.turn(turn)
        robot.move()
    pretty_print(panels)
    return len(panels)


def pretty_print(panels):
    # Gamble kinda payed off
    from_x = float("inf")
    to_x = 0
    from_y = float("inf")
    to_y = 0
    for coords in panels:
        if coords[0] < from_x:
            from_x = coords[0]
        elif coords[0] > to_x:
            to_x = coords[0]
        if coords[1] < from_y:
            from_y = coords[1]
        elif coords[1] > to_y:
            to_y = coords[1]
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
            if (x, y) in panels:
                if panels[(x, y)] == 0:
                    print("⬛", end="")
                else:
                    print("⬜", end="")
            else:
                print("⬛", end="")
        print()


print(solve_day_11("input.txt"))
