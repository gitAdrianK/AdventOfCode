import re
from intcode_computer import IntCodeComputer


def solve_day_05(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    computer.run()


solve_day_05("input.txt")
