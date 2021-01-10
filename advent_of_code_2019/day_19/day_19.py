from intcode_computer import IntCodeComputer
import re


def solve_day_17(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    size = 50
    p1 = 0
    for x in range(size):
        for y in range(size):
            # I have no clue why I need three inputs, but I do
            computer.write([0, x, y])
            computer.run()
            result = computer.read()[0]
            p1 += result
            computer.reset()
    return (p1, 0)


print(solve_day_17("input.txt"))
