import re


def solve_day_06(input):
    orbits = {}
    regex = re.compile("[\d|\w]+")
    f = open(input, "r")
    p1 = 0
    p2 = 0
    set_you = None
    set_san = None
    for line in f.readlines():
        orbit = regex.findall(line)
        orbits[orbit[1]] = orbit[0]
    for orbit in orbits:
        set_ = orbit_set(orbit, orbits)
        p1 += len(set_)
        if orbit == "SAN":
            set_san = set_
        if orbit == "YOU":
            set_you = set_
    if set_you is not None and set_san is not None:
        p2 = len(orbital_trasfers(
            set_san, orbits["SAN"], set_you, orbits["YOU"], orbits))
    return (p1, p2)


def orbit_set(orbit, orbits, set_=None):
    if set_ is None:
        set_ = set()
    if orbit not in orbits:
        return set_
    else:
        set_.add(orbit)
        return orbit_set(orbits[orbit], orbits, set_)


def orbital_trasfers(set_a, start_a, set_b, start_b, orbits):
    set_common = set_a.intersection(set_b)
    set_a = travese_until_common(start_a, orbits, set_common)
    set_b = travese_until_common(start_b, orbits, set_common)
    return set_a.union(set_b)


def travese_until_common(orbit, orbits, common, set_=None):
    if set_ is None:
        set_ = set()
    if orbit in common:
        return set_
    else:
        set_.add(orbit)
        return travese_until_common(orbits[orbit], orbits, common, set_)


# print(solve_day_06("test_input_0.txt"))
# print(solve_day_06("test_input_1.txt"))
print(solve_day_06("input.txt"))
