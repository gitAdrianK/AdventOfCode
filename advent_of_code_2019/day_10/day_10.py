def solve_day_10(input):
    f = open(input, "r")
    astroids = []
    p1 = (0, 0)
    p1_visible = 0
    for line in f.readlines():
        astroids.append(line.replace("\n", ""))
    fractions = generate_fractions(len(astroids))
    for y, col in enumerate(astroids):
        for x, row in enumerate(col):
            if row == "#":
                visible = count_visible(x, y, fractions, astroids)
                if visible > p1_visible:
                    p1 = (x, y)
                    p1_visible = visible
    p2 = (0, 0)
    astroids[p1[1]] = astroids[p1[1]][:p1[0]]+"O"+astroids[p1[1]][p1[0]+1:]
    destroyed = 0
    limit = 200
    sector = 0
    for_sector = [
        # 0,1 are values for the axis
        # 2,3 are multipliers for sectors
        # 4,5 are fraction order
        # can I improve this, yes, will I do it, ¯\_(ツ)_/¯
        (0, -1, 1, -1, 0, 1),
        (1, 0, 1, 1, 1, 0),
        (0, 1, -1, 1, 0, 1),
        (-1, 0, -1, -1, 1, 0),
    ]
    while destroyed < limit:
        sec = for_sector[sector]
        astroid = sees_astroid(p1[0], p1[1], (sec[0], sec[1]), astroids)
        if astroid[0]:
            astroids[astroid[2]] = astroids[astroid[2]][:astroid[1]] + \
                "_"+astroids[astroid[2]][astroid[1]+1:]
            destroyed += 1
            if destroyed == limit:
                p2 = astroid
                break
        for fraction in fractions:
            astroid = sees_astroid(
                p1[0], p1[1], (fraction[sec[4]]*sec[2], fraction[sec[5]]*sec[3]), astroids)
            if astroid[0]:
                astroids[astroid[2]] = astroids[astroid[2]][:astroid[1]
                                                            ]+"_"+astroids[astroid[2]][astroid[1]+1:]
                destroyed += 1
                if destroyed == limit:
                    p2 = astroid
                    break
        sector = ((sector+1) % 4)
    return (p1_visible, p2[1]*100+p2[2])


def generate_fractions(limit):
    fractions = []
    int_fractions = []
    for i in range(1, limit):
        for j in range(1, limit):
            if i/j in fractions:
                continue
            fractions.append(i/j)
            int_fractions.append((i, j))
    int_fractions = [x for _, x in sorted(zip(fractions, int_fractions))]
    return int_fractions


def count_visible(x, y, fractions, astroids):
    count = 0
    count += sees_astroid(x, y, (1, 0), astroids)[0]
    count += sees_astroid(x, y, (0, 1), astroids)[0]
    count += sees_astroid(x, y, (-1, 0), astroids)[0]
    count += sees_astroid(x, y, (0, -1), astroids)[0]
    for fraction in fractions:
        count += sees_astroid(x, y, (fraction[0], fraction[1]), astroids)[0]
        count += sees_astroid(x, y, (fraction[0], -fraction[1]), astroids)[0]
        count += sees_astroid(x, y, (-fraction[0], fraction[1]), astroids)[0]
        count += sees_astroid(x, y, (-fraction[0], -fraction[1]), astroids)[0]
    return count


def sees_astroid(x, y, coords, astroids):
    while True:
        try:
            x += coords[0]
            y += coords[1]
            if x < 0 or y < 0:
                return (False, 0, 0)
            if astroids[y][x] == "#":
                return (True, x, y)
        except IndexError:
            return (False, 0, 0)


print(solve_day_10("input.txt"))
