from intcode_computer import IntCodeComputer
import re


def solve_day_17(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    computer.run()
    camera = computer.read()
    lst = []
    line = []
    for c in camera:
        if c == 10:
            lst.append(line)
            line = []
        else:
            line.append(c)
    p1 = 0
    for y, cy in enumerate(lst[1:-2], 1):
        for x, cx in enumerate(cy[1:-1], 1):
            if cx == 35:
                if lst[y-1][x] == 35 and lst[y+1][x] == 35 and lst[y][x-1] == 35 and lst[y][x+1] == 35:
                    lst[y][x] = ord("O")
                    p1 += x*y
    for cy in lst:
        for cx in cy:
            print(chr(cx), end="")
        print()
    return (p1, 0)


print(solve_day_17("input.txt"))
