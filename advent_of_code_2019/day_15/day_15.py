from intcode_computer import IntCodeComputer, Status
import re


class Droid:
    def __init__(self):
        self.pos = (0, 0)
        self.path = []

    def move(self, direction, is_backtrack=False):
        if not is_backtrack:
            self.path.append(direction)
        if direction == 1:
            self.pos = (self.pos[0], self.pos[1]-1)
        elif direction == 2:
            self.pos = (self.pos[0], self.pos[1]+1)
        elif direction == 3:
            self.pos = (self.pos[0]-1, self.pos[1])
        elif direction == 4:
            self.pos = (self.pos[0]+1, self.pos[1])

    def backtrack(self):
        if len(self.path) == 0:
            return
        last = self.path.pop()
        if last == 1:
            self.move(2, True)
            return 2
        elif last == 2:
            self.move(1, True)
            return 1
        elif last == 3:
            self.move(4, True)
            return 4
        elif last == 4:
            self.move(3, True)
            return 3


def solve_day_15(input):
    droid = Droid()
    tiles = {(0, 0): "❌"}
    coords = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    computer = IntCodeComputer(regex.findall(f.readline()))
    p1 = None
    while computer.status != Status.TERMINATED:
        p1 = scout_area(computer, coords, droid, tiles)
    print_area(None, tiles)
    p2 = flood_area([p1[0]], coords, tiles)
    return (p1[1], p2)


def scout_area(computer, coords, droid, tiles, depth=1):
    oxygen = None
    for d in [1, 2, 3, 4]:
        target = (droid.pos[0]+coords[d][0], droid.pos[1]+coords[d][1])
        if target in tiles:
            continue
        computer.write(d)
        computer.run()
        out = computer.read()[0]
        if out == 0:
            tiles[target] = "⬜"
        elif out == 1:
            tiles[target] = "⬛"
            droid.move(d)
            ox = scout_area(computer, coords, droid, tiles, depth+1)
            if ox is not None:
                oxygen = ox
        elif out == 2:
            tiles[target] = "⭕"
            oxygen = (target, depth)
            droid.move(d)
            scout_area(computer, coords, droid, tiles, depth+1)
    back = droid.backtrack()
    if back is not None:
        computer.write(back)
        computer.run()
        computer.read()
    else:
        computer.status = Status.TERMINATED
    return oxygen


def flood_area(curr, coords, tiles, depth=0):
    if len(curr) == 0:
        return depth-1
    next = []
    for c in curr:
        for d in [1, 2, 3, 4]:
            n = (c[0]+coords[d][0], c[1]+coords[d][1])
            if n in tiles and tiles[n] == "⬛":
                tiles[n] = "0️⃣ "
                next.append(n)
    return flood_area(next, coords, tiles, depth+1)


def print_area(droid, tiles):
    xs = []
    ys = []
    for tile in tiles:
        xs.append(tile[0])
        ys.append(tile[1])
    xs.sort()
    ys.sort()
    lo_hi = [xs[0], xs[-1], ys[0], ys[-1]]
    for y in range(lo_hi[2]-1, lo_hi[3]+2):
        for x in range(lo_hi[0]-1, lo_hi[1]+2):
            if droid is not None and droid.pos[0] == x and droid.pos[1] == y:
                print("➕", end="")
            else:
                if (x, y) in tiles:
                    print(tiles[(x, y)], end="")
                else:
                    print("  ", end="")
        print()


print(solve_day_15("input.txt"))
