from itertools import permutations, count
from math import lcm
import re


class Planet:

    x = None
    y = None
    z = None
    vx = None
    vy = None
    vz = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def apply_gravity(self, other):
        self.vx += sorted([-1, other.x-self.x, 1])[1]
        self.vy += sorted([-1, other.y-self.y, 1])[1]
        self.vz += sorted([-1, other.z-self.z, 1])[1]

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z)) * (abs(self.vx)+abs(self.vy)+abs(self.vz))


def solve_day_12(input, energy_at):
    planets = []
    start = []
    looping = []
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    for line in f.readlines():
        xyz = regex.findall(line)
        planets.append(Planet(int(xyz[0]), int(xyz[1]), int(xyz[2])))
        start.append(Planet(int(xyz[0]), int(xyz[1]), int(xyz[2])))
        looping.append([0, 0, 0])
    p1 = 0
    for i in count(start=1):
        for p in permutations(planets, 2):
            p[0].apply_gravity(p[1])
        for j, planet in enumerate(planets):
            planet.apply_velocity()
            loop = looping[j]
            if planet.x == start[j].x and planet.vx == start[j].vx and loop[0] == 0:
                loop[0] = i
            if planet.y == start[j].y and planet.vy == start[j].vy and loop[1] == 0:
                loop[1] = i
            if planet.z == start[j].z and planet.vz == start[j].vz and loop[2] == 0:
                loop[2] = i
        if i == energy_at:
            for planet in planets:
                p1 += planet.get_energy()
        loops_found = True
        for loop in looping:
            if loop.count(0) != 0:
                loops_found = False
                break
        if p1 != 0 and loops_found:
            break
    flatten = []
    for loop in looping:
        for l in loop:
            flatten.append(l)
    while len(flatten) > 1:
        flatten.append(lcm(flatten[0], flatten[1]))
        flatten = flatten[2:]
    p2 = flatten[0]
    return (p1, p2)


print(solve_day_12("test_input_0.txt", 10))
print(solve_day_12("test_input_1.txt", 100))
print(solve_day_12("input.txt", 1000))
