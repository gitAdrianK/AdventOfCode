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
    # This was just for pretty printing so see how things look, but I am now using it
    # to manually solve part 2
    for cy in lst:
        for cx in cy:
            if cx == ord("."):
                print("⬛", end="")
            else:
                print("⬜", end="")
        print()
    # and after a little puzzling we get (see Scaffold.png)
    # "A"=65, "B"=66, "C"=67, ","=44, "\n"=10
    # "L"=76, "R"=82
    # "12"=49 50, "8"=56, "6"=54, "4"=52
    # "n" = 110
    # A = L12,L12,L6,L6
    # B = L12,L6,R12,R8
    # C = R8,R4,L12
    # A,C,A,B,C,A,B,C,A,B
    computer.reset()
    computer.memory[0] = 2
    instructions = [
        #A   ,   C   ,   A   ,   B   ,   C   ,   A   ,   B   ,   C   ,   A   ,   B  \n
        65, 44, 67, 44, 65, 44, 66, 44, 67, 44, 65, 44, 66, 44, 67, 44, 65, 44, 66, 10,
        #L   ,   1   2   ,   L   ,   1   2   ,   L   ,   6   ,   L   ,   6  \n
        76, 44, 49, 50, 44, 76, 44, 49, 50, 44, 76, 44, 54, 44, 76, 44, 54, 10,
        #L   ,   1   2   ,   L   ,   6   ,   R   ,   1   2   ,   R   ,   8  \n
        76, 44, 49, 50, 44, 76, 44, 54, 44, 82, 44, 49, 50, 44, 82, 44, 56, 10,
        #R   ,   8   ,   R   ,   4   ,   L   ,   1   2  \n
        82, 44, 56, 44, 82, 44, 52, 44, 76, 44, 49, 50, 10,
        #n,  \n
        110, 10
    ]
    computer.write(instructions)
    computer.run()
    p2 = computer.read()[-1]
    return (p1, p2)


print(solve_day_17("input.txt"))
