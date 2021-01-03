from itertools import permutations
from functools import reduce
from math import lcm
import re


class Moon:
    def __init__(self, x, y, z):
        self.start = [x, y, z]
        self.pos = self.start[:]
        self.loop = [None, None, None]
        self.vel = [0, 0, 0]
        self.iter = 1

    def apply_gravity(self, other):
        for i in range(3):
            self.vel[i] += sorted([-1, other.pos[i]-self.pos[i], 1])[1]

    def apply_velocity(self):
        self.iter += 1
        for i in range(3):
            self.pos[i] += self.vel[i]

    def get_energy(self):
        pot = 0
        kin = 0
        for i in range(3):
            pot += abs(self.pos[i])
            kin += abs(self.vel[i])
        return pot*kin


def solve_day_12(input, energy_at):
    moons = []
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    for line in f.readlines():
        xyz = regex.findall(line)
        moons.append(Moon(int(xyz[0]), int(xyz[1]), int(xyz[2])))
    p1 = 0
    lcms = {}
    i = 0
    while len(lcms) < 3:
        for p in permutations(moons, 2):
            p[0].apply_gravity(p[1])
        for planet in moons:
            planet.apply_velocity()
        i += 1
        if i == energy_at:
            for planet in moons:
                p1 += planet.get_energy()
        for j in range(3):
            # Stolen from https://gitlab.com/scul/Advent-of-Code-2019/blob/master/day12/12.py
            # My own attempt found the right periods but messed up the lcms somehow
            if moons[0].pos[j] == moons[0].start[j] and \
                    moons[1].pos[j] == moons[1].start[j] and \
                    moons[2].pos[j] == moons[2].start[j] and \
                    moons[3].pos[j] == moons[3].start[j] and \
                    j not in lcms:
                l = lcm_([m.iter for m in moons])
                lcms[j] = l
    p2 = lcm_(l for l in lcms.values())
    return (p1, p2)


def lcm_(lst):
    return reduce(lcm, lst)


# print(solve_day_12("test_input_0.txt", 10))
# print(solve_day_12("test_input_1.txt", 100))
print(solve_day_12("input.txt", 1000))
