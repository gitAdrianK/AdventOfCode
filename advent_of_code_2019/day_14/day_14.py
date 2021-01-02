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
        lst.append(int(product[0]))
        for educt in educts:
            educt = educt.split(" ")
            educt = (educt[1], int(educt[0]))
            lst.append(educt)
        reactions[product[1]] = lst
    p1 = 0
    created = ["FUEL"]
    leftover = {}
    for reaction in reactions:
        if reaction == "ORE" or reaction == "FUEL":
            continue
        leftover[reaction] = 0
    while len(created) > 0:
        product = created.pop()
        if product in reactions:
            educts = reactions[product][1:]
            for educt in educts:
                if educt[0] == "ORE":
                    p1 += educt[1]
                else:
                    have = leftover[educt[0]]
                    needs = educt[1]
                    diff = have-needs
                    if diff >= 0:
                        leftover[educt[0]] = diff
                    else:
                        creates = reactions[educt[0]][0]
                        times = 0
                        while diff < 0:
                            diff += creates
                            times += 1
                        leftover[educt[0]] = diff
                        for _ in range(times):
                            created.append(educt[0])
    return p1


print(solve_day_14("input.txt"))
