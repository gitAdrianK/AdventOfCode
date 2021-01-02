from io import StringIO
from intcode_computer import IntCodeComputer, Status
import re
import sys


def solve_day_13(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    ts = play(computer,  {})
    tiles = ts[0]
    score = ts[1]
    print_arcade(tiles)
    p1 = sum(value == 2 for value in tiles.values())
    computer.reset()
    computer.memory[0] = 2
    old_stdin = sys.stdin
    while computer.status != Status.TERMINATED:
        input_ = str(get_joystick(tiles))+"\npause\n"
        new_stdin = StringIO(input_)
        sys.stdin = new_stdin
        ts = play(computer, tiles)
        tiles = ts[0]
        score = ts[1]
        # print_arcade(tiles)
    sys.stdin = old_stdin
    return (p1, score)


def play(computer, tiles):
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    computer.run()
    sys.stdout = old_stdout
    output = new_stdout.getvalue()
    output = re.sub("[^-0-9\n]", "", output)
    output = output.split("\n")
    score = 0
    for out in range(0, len(output)-3, 3):
        if output[out] == "-1" and output[out+1] == "0":
            score = output[out+2]
            continue
        tiles[(int(output[out]), int(output[out+1]))] = int(output[out+2])
    return (tiles, score)


def get_joystick(tiles):
    ball = None
    paddle = None
    for tile in tiles:
        if tiles[tile] == 3:
            ball = tile[0]
        elif tiles[tile] == 4:
            paddle = tile[0]
    joystick = 0
    if ball > paddle:
        joystick = -1
    elif ball < paddle:
        joystick = 1
    return joystick


def print_arcade(tiles):
    from_x = float("inf")
    to_x = 0
    from_y = float("inf")
    to_y = 0
    for coords in tiles:
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
            if (x, y) in tiles:
                if tiles[(x, y)] == 0:
                    print("⬛", end="")
                elif tiles[(x, y)] == 1:
                    print("⚫", end="")
                elif tiles[(x, y)] == 2:
                    print("⬜", end="")
                elif tiles[(x, y)] == 3:
                    print("➖", end="")
                elif tiles[(x, y)] == 4:
                    print("⚪", end="")
        print()


print(solve_day_13("input.txt"))
