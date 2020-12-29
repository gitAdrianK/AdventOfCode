from intcode_computer import IntCodeComputer
import re


def solve_day_09(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    computer.run()

# For part 1 input 1, for part 2 input 2
solve_day_09("input.txt")
