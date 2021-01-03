from intcode_computer import IntCodeComputer
import re


def solve_day_09(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    computer.write(1)
    computer.run()
    p1 = computer.read()[0]
    computer.reset()
    computer.write(2)
    computer.run()
    p2 = computer.read()[0]
    return (p1, p2)


print(solve_day_09("input.txt"))
