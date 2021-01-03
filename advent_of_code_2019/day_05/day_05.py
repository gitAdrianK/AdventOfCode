import re
from intcode_computer import IntCodeComputer


def solve_day_05(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    computer.write(1)
    computer.run()
    p1 = computer.read()[-1]
    computer.reset()
    computer.write(5)
    computer.run()
    p2 = computer.read()[0]
    return (p1, p2)


print(solve_day_05("input.txt"))
