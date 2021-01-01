from itertools import permutations
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
        diff = self.x-other.x
        if diff > 0:
            self.vx -= 1
        elif diff < 0:
            self.vx += 1
        diff = self.y-other.y
        if diff > 0:
            self.vy -= 1
        elif diff < 0:
            self.vy += 1
        diff = self.z-other.z
        if diff > 0:
            self.vz -= 1
        elif diff < 0:
            self.vz += 1

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z)) * (abs(self.vx)+abs(self.vy)+abs(self.vz))


def solve_day_12(input):
    planets = []
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    for line in f.readlines():
        xyz = regex.findall(line)
        planets.append(Planet(int(xyz[0]), int(xyz[1]), int(xyz[2])))
    for _ in range(1000):
        for p in permutations(planets, 2):
            p[0].apply_gravity(p[1])
        for planet in planets:
            planet.apply_velocity()
    p1 = 0
    for planet in planets:
        p1 += planet.get_energy()
    return p1


print(solve_day_12("input.txt"))
