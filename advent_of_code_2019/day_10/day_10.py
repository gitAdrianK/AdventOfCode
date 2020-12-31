def solve_day_10(input):
    f = open(input, "r")
    astroids = []
    p1 = (0, 0)
    p1_visible = 0
    for line in f.readlines():
        astroids.append(line.replace("\n", ""))
    for y, col in enumerate(astroids):
        for x, row in enumerate(col):
            if row == "#":
                visible = count_visible(x, y, astroids)
                if visible > p1_visible:
                    p1 = (x, y)
                    p1_visible = visible
    return (p1, p1_visible)


def count_visible(x, y, astroids):
    count = 0
    count += sees_astroid(x, y, (1, 0), astroids)
    count += sees_astroid(x, y, (0, 1), astroids)
    count += sees_astroid(x, y, (-1, 0), astroids)
    count += sees_astroid(x, y, (0, -1), astroids)
    fractions = []
    for i in range(1, len(astroids)):
        for j in range(1, len(astroids)):
            if i/j in fractions:
                continue
            count += sees_astroid(x, y, (i, j), astroids)
            count += sees_astroid(x, y, (i, -j), astroids)
            count += sees_astroid(x, y, (-i, j), astroids)
            count += sees_astroid(x, y, (-i, -j), astroids)
            fractions.append(i/j)
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
