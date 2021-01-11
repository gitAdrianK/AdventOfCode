import re


def solve_day_18(input):
    f = open(input, "r")
    vault = []
    doors = set()
    to_collect = set()
    pos = None
    for y, line in enumerate(f.readlines()):
        to_collect.update(re.findall("[a-z]", line))
        line = line.replace("\n", "")
        for x, char in enumerate(line):
            if re.match("@", char):
                pos = (x, y)
                line = line.replace("@", ".")
            elif re.match("[A-Z]", char):
                doors.add(char)
        vault.append(line)
    print()
    print_vault(vault, pos)
    print("To collect", to_collect, len(to_collect))
    print("Start pos", pos)
    print("Doors", doors, len(doors))
    p1 = [float("inf")]
    traverse_vault(vault, [], len(to_collect), pos, p1)
    return (p1[0], 0)


def traverse_vault(vault, keys, to_collect, start, bound, steps=0):
    if len(keys) == to_collect:
        if steps < bound[0]:
            bound[0] = steps
        print(keys, steps)
        return
    to_visit = []
    to_visit.append((start, steps))
    visited = []
    found_keys = []
    while len(to_visit) > 0:
        curr, step = to_visit.pop()
        if step >= bound[0]:
                continue
        if curr in visited:
            continue
        visited.append(curr)
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next = (curr[0]+d[0], curr[1]+d[1])
            if next in visited:
                continue
            tile = vault[next[1]][next[0]]
            if tile == ".":
                to_visit.append((next, step+1))
            elif re.match("[a-z]", tile):
                if tile not in keys:
                    found_keys.append((next, step+1, tile))
                else:
                    to_visit.append((next, step+1))
            elif re.match("[A-Z]", tile) and tile.lower() in keys:
                to_visit.append((next, step+1))
    found_keys.sort(key=lambda k: k[1])
    for k in found_keys:
        if k[1] < bound[0]:
            keys_new = keys[:]
            keys_new.append(k[2])
            traverse_vault(vault, keys_new, to_collect, k[0], bound, k[1])


def print_vault(vault, pos):
    for y, v in enumerate(vault):
        for x, c in enumerate(v):
            if (x, y) == pos:
                print("@", end="")
            else:
                print(c, end="")
        print()


#print(solve_day_18("test_input_0.txt"))  # 8
#print(solve_day_18("test_input_1.txt"))  # 86
#print(solve_day_18("test_input_2.txt"))  # 132
print(solve_day_18("test_input_3.txt"))  # 136
#print(solve_day_18("test_input_4.txt"))  # 81
#print(solve_day_18("input.txt"))
