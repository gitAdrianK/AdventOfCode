from io import StringIO
from intcode_computer import IntCodeComputer
import re
import sys


def solve_day_13(input):
    tiles = {}
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    computer.run()
    sys.stdout = old_stdout
    output = new_stdout.getvalue().split("\n")
    for out in range(0, len(output)-3, 3):
        tiles[(output[out], output[out+1])] = output[out+2]
    p1 = sum(value == "2" for value in tiles.values())
    return p1


print(solve_day_13("input.txt"))
