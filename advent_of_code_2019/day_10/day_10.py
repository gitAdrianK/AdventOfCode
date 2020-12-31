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
    return (p1, p1_visible)


def generate_fractions(limit):
    fractions = []
    int_fractions = []
    for i in range(1, limit):
        for j in range(1, limit):
            if i/j in fractions:
                continue
            fractions.append(i/j)
            int_fractions.append((i, j))
    return int_fractions


def count_visible(x, y, fractions, astroids):
    count = 0
    count += sees_astroid(x, y, (1, 0), astroids)
    count += sees_astroid(x, y, (0, 1), astroids)
    count += sees_astroid(x, y, (-1, 0), astroids)
    count += sees_astroid(x, y, (0, -1), astroids)
    for fraction in fractions:
        count += sees_astroid(x, y, (fraction[0], fraction[1]), astroids)
        count += sees_astroid(x, y, (fraction[0], -fraction[1]), astroids)
        count += sees_astroid(x, y, (-fraction[0], fraction[1]), astroids)
        count += sees_astroid(x, y, (-fraction[0], -fraction[1]), astroids)
    return count


def sees_astroid(x, y, coords, astroids):
    while True:
        try:
            x += coords[0]
            y += coords[1]
            if x < 0 or y < 0:
                return False
            if astroids[y][x] == "#":
                return True
        except IndexError:
            return False


print(solve_day_10("input.txt"))
