import re


def solve_day_06(input):
    orbits = {}
    regex = re.compile("[\d|\w]+")
    f = open(input, "r")
    p1 = 0
    for line in f.readlines():
        orbit = regex.findall(line)
        orbits[orbit[1]] = orbit[0]
    for orbit in orbits:
        p1 += orbit_depth(orbit, orbits)
    return p1


def orbit_depth(orbit, orbits, depth=0):
    if orbit not in orbits:
        return depth
    else:
        return orbit_depth(orbits[orbit], orbits, depth+1)


print(solve_day_06("test_input_0.txt"))
print(solve_day_06("input.txt"))
