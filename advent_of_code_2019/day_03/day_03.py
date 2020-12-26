import re


def solve_day_03(input):
    regex = re.compile("\w\d+")
    f = open(input, "r")
    cables = get_cables(regex.findall(f.readline()))
    cable_one_horizontal = cables[0]
    cable_one_vertical = cables[1]
    cables = get_cables(regex.findall(f.readline()))
    cable_two_horizontal = cables[0]
    cable_two_vertical = cables[1]
    # print(cable_one_horizontal)
    # print(cable_one_vertical)
    # print(cable_two_horizontal)
    # print(cable_two_vertical)
    manhattan = float("inf")
    for vertical in cable_one_vertical:
        for horizontal in cable_two_horizontal:
            if are_intersecting(vertical, horizontal):
                m = get_manhattan(vertical, horizontal)
                if m < manhattan:
                    manhattan = m
    for vertical in cable_two_vertical:
        for horizontal in cable_one_horizontal:
            if are_intersecting(vertical, horizontal):
                m = get_manhattan(vertical, horizontal)
                if m < manhattan:
                    manhattan = m

    return (manhattan, 0)


def are_intersecting(vertical, horizontal):
    if horizontal[0] == (0,0) and vertical[0] == (0,0):
        return False
    if vertical[0][1] <= horizontal[0][1] <= vertical[1][1]:
        if horizontal[0][0] <= vertical[0][0] <= horizontal[1][0]:
            return True


def get_manhattan(vertical, horizontal):
    return abs(vertical[0][0]) + abs(horizontal[0][1])


def get_cables(cables):
    horizontal = []
    vertical = []
    point = (0, 0)
    prev_point = (0, 0)
    for cable in cables:
        direction = cable[0]
        amount = int(cable[1:])
        if direction == "U":
            point = (point[0], point[1]+amount)
            vertical.append((prev_point, point))
            prev_point = point
        elif direction == "D":
            point = (point[0], point[1]-amount)
            vertical.append((point, prev_point))
            prev_point = point
        elif direction == "L":
            point = (point[0]-amount, point[1])
            horizontal.append((point, prev_point))
            prev_point = point
        elif direction == "R":
            point = (point[0]+amount, point[1])
            horizontal.append((prev_point, point))
            prev_point = point
    return (horizontal, vertical)


print(solve_day_03("test_input_0.txt"))
print(solve_day_03("test_input_1.txt"))
print(solve_day_03("test_input_2.txt"))
print(solve_day_03("input.txt"))
