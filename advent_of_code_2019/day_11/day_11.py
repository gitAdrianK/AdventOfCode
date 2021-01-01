from io import StringIO
from intcode_computer import IntCodeComputer, Status
from enum import Enum, IntEnum, Flag
import re
import sys


class Facing(IntEnum):
    UP = 3
    LEFT = 2
    DOWN = 1
    RIGHT = 0


class Turn(Enum):
    LEFT = 0
    RIGHT = 1


class Robot:

    facing = None
    x = None
    y = None

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
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    # Instead of using a set for what panels have been painted
    # to see how many panels the robot paints at least once
    # I am just gonna gamble that part 2 asks about what was painted
    # so I can just go and print this dict
    panels = {}
    robot = Robot()
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    start = "0\npause\n"
    sys.stdin = StringIO(start)
    new_stdout = StringIO()
    sys.stdout = new_stdout
    computer.run()
    output = re.sub("[^0-9\n]", "", new_stdout.getvalue())
    output = output.split("\n")
    paint_as = output[0]
    turn = output[1]
    panels[(robot.x, robot.y)] = paint_as
    robot.turn(int(turn))
    robot.move()
    while computer.status != Status.TERMINATED:
        new_stdout = StringIO()
        sys.stdout = new_stdout
        camera = ""
        if (robot.x, robot.y) in panels:
            camera = str(panels[(robot.x, robot.y)])
        else:
            camera = "0"
        camera += "\npause\n"
        sys.stdin = StringIO(camera)
        computer.run()
        output = re.sub("[^0-9\n]", "", new_stdout.getvalue())
        output = output.split("\n")
        paint_as = output[0]
        turn = output[1]
        panels[(robot.x, robot.y)] = paint_as
        robot.turn(int(turn))
        robot.move()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    return len(panels)


print(solve_day_11("input.txt"))
