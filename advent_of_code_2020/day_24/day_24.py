import re
from enum import Flag


class Flipped(Flag):
    BLACK = True
    WHITE = False


def solveDay24(input):
    # Setup
    tiles = {}
    regex = re.compile("e|se|sw|w|nw|ne")
    f = open(input, "r")
    for line in list(f.readlines()):
        coords = (0, 0)
        for direction in re.findall(regex, line):
            if direction == "e":
                coords = tuple(map(sum, zip(coords, (1, 0))))
            elif direction == "se":
                coords = tuple(map(sum, zip(coords, (1, -1))))
            elif direction == "sw":
                coords = tuple(map(sum, zip(coords, (0, -1))))
            elif direction == "w":
                coords = tuple(map(sum, zip(coords, (-1, 0))))
            elif direction == "nw":
                coords = tuple(map(sum, zip(coords, (-1, 1))))
            elif direction == "ne":
                coords = tuple(map(sum, zip(coords, (0, 1))))
        if coords in tiles:
            tiles[coords] = Flipped(not tiles[coords])
        else:
            tiles[coords] = Flipped.BLACK
    p1 = sum(v == Flipped.BLACK for v in tiles.values())
    # Okay so lets be honest, theres ways to make this better, like adding an "active"
    # state to the tiles, since a white tile with no black neighbors could never flip we don't
    # need to ever look at it or extend the ring around it, but this is now the third time
    # I am playing some form of Conway's Game of Life, I cannot be asked to do optimizations like that.
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
    for _ in range(100):
        tiles = extendTiles(tiles, neighbors)
        tiles = flipTiles(tiles, neighbors)
    p2 = sum(v == Flipped.BLACK for v in tiles.values())
    return (p1, p2)


def extendTiles(tiles, neighbors):
    new_tiles = {}
    for tile in tiles:
        new_tiles[tile] = tiles[tile]
        for neighbor in neighbors:
            neighbor_coords = tuple(map(sum, zip(tile, neighbor)))
            if neighbor_coords not in tiles:
                new_tiles[neighbor_coords] = Flipped.WHITE
    return new_tiles


def flipTiles(tiles, neighbors):
    new_tiles = {}
    for tile in tiles:
        neighbor_count = 0
        for neighbor in neighbors:
            neighbor_coords = tuple(map(sum, zip(tile, neighbor)))
            if neighbor_coords in tiles and tiles[neighbor_coords]:
                neighbor_count += 1
        new_tiles[tile] = tiles[tile]
        if tiles[tile]:
            if neighbor_count == 0 or neighbor_count > 2:
                new_tiles[tile] = Flipped.WHITE
        else:
            if neighbor_count == 2:
                new_tiles[tile] = Flipped.BLACK
    return new_tiles


assert((10, 2208) == solveDay24("test_input.txt"))
print(solveDay24("input.txt"))
