import re

def solveDay24(input):
    # Setup
    p1 = 0
    tiles = set()
    regex = re.compile("e|se|sw|w|nw|ne")
    f = open(input, "r")
    for line in list(f.readlines()):

        coords = (0,0)
        for direction in re.findall(regex, line):
            if direction == "e":
                coords = tuple(map(sum, zip(coords, (1,0))))
            elif direction == "se":
                coords = tuple(map(sum, zip(coords, (1,-1))))
            elif direction == "sw":
                coords = tuple(map(sum, zip(coords, (0,-1))))
            elif direction == "w":
                coords = tuple(map(sum, zip(coords, (-1,0))))
            elif direction == "nw":
                coords = tuple(map(sum, zip(coords, (-1,1))))
            elif direction == "ne":
                coords = tuple(map(sum, zip(coords, (0,1))))
        if coords in tiles:
            tiles.remove(coords)
        else:
            tiles.add(coords)
    p1 = len(tiles)
    return (p1, 0)


assert((10, 0) == solveDay24("test_input.txt"))
print(solveDay24("input.txt"))
