from collections import defaultdict
from math import ceil
import re


def solve_day_14(input):
    reactions = {}
    f = open(input, "r")
    regex = re.compile("\d+ \w+")
    for line in f.readlines():
        reaction = regex.findall(line)
        product = reaction[-1].split(" ")
        educts = reaction[:-1]
        lst = []
        for educt in educts:
            educt = educt.split(" ")
            educt = (educt[1], int(educt[0]))
            lst.append(educt)
        reactions[product[1]] = [int(product[0]),lst]
    p1 = create_fuel(reactions)
    p2 = 2
    LIMIT = 1_000_000_000_000
    while (used := create_fuel(reactions, p2)) <= LIMIT:
        p2 = max(p2*LIMIT//used, p2+1)
    return (p1, p2-1)


def create_fuel(reactions, fuel=1):
    leftover = defaultdict(int)
    want = [("FUEL", fuel)]
    while len(want) > 0:
        product, need = want.pop(0)
        have = leftover[product]
        if product == "ORE":
            leftover["ORE"] = have+need
            continue
        if have-need >= 0:
            leftover[product] = have-need
            continue
        else:
            need = need-have
            leftover[product] = 0
        reaction = reactions[product]
        multiplier = ceil(need/reaction[0])
        leftover[product] = reaction[0]*multiplier - need
        for educt in reaction[1]:
            want.append((educt[0], educt[1]*multiplier))
    return leftover["ORE"]


print(solve_day_14("test_input_0.txt"))
print(solve_day_14("test_input_1.txt"))
print(solve_day_14("test_input_2.txt"))
print(solve_day_14("test_input_3.txt"))
print(solve_day_14("test_input_4.txt"))
print(solve_day_14("input.txt"))
