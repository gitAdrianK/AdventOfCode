import re


def solve_day_03(input):
    regex = re.compile("\w\d+")
    f = open(input, "r")
    cables = get_cables(regex.findall(f.readline()))
    one_horizontals = cables[0]
    one_verticals = cables[1]
    cable_one = cables[2]
    cables = get_cables(regex.findall(f.readline()))
    two_horizontals = cables[0]
    two_verticals = cables[1]
    cable_two = cables[2]
    intersections = get_intersections(one_verticals, two_horizontals)
    intersections.extend(get_intersections(two_verticals, one_horizontals))
    manhattan = float("inf")
    signal_delay = float("inf")
    for intersection in intersections:
        m = get_manhattan(intersection)
        if m < manhattan:
            manhattan = m
        delay_one = get_delay(cable_one, intersection)
        delay_two = get_delay(cable_two, intersection)
        s = delay_one + delay_two
        if s < signal_delay:
            signal_delay = s
    return (manhattan, signal_delay)


def get_intersections(verticals, horizontals):
    intersections = []
    for vertical in verticals:
        for horizontal in horizontals:
            if are_intersecting(vertical, horizontal):
                intersections.append((vertical[0][0], horizontal[0][1]))
    return intersections


def are_intersecting(vertical, horizontal):
    if horizontal[0] == (0, 0) and vertical[0] == (0, 0):
        return False
    if vertical[0][1] <= horizontal[0][1] <= vertical[1][1]:
        if horizontal[0][0] <= vertical[0][0] <= horizontal[1][0]:
            return True


def get_manhattan(point):
    return abs(point[0]) + abs(point[1])


def get_delay(cable, point):
    delay = 0
    for c in cable:
        if c[0][0] <= point[0] <= c[1][0] or c[0][0] >= point[0] >= c[1][0]:
            if c[0][1] <= point[1] <= c[1][1] or c[0][1] >= point[1] >= c[1][1]:
                x_delay = abs(c[0][0] - point[0])
                y_delay = abs(c[0][1] - point[1])
                delay += x_delay + y_delay
                return delay
        x_delay = abs(c[0][0] - c[1][0])
        y_delay = abs(c[0][1] - c[1][1])
        delay += x_delay + y_delay
    return float("inf")


def get_cables(cables):
    horizontal = []
    vertical = []
    combined = []
    point = (0, 0)
    prev_point = (0, 0)
    for cable in cables:
        direction = cable[0]
        amount = int(cable[1:])
        if direction == "U":
            point = (point[0], point[1]+amount)
            vertical.append((prev_point, point))
            combined.append((prev_point, point))
            prev_point = point
        elif direction == "D":
            point = (point[0], point[1]-amount)
            vertical.append((point, prev_point))
            combined.append((prev_point, point))
            prev_point = point
        elif direction == "L":
            point = (point[0]-amount, point[1])
            horizontal.append((point, prev_point))
            combined.append((prev_point, point))
            prev_point = point
        elif direction == "R":
            point = (point[0]+amount, point[1])
            horizontal.append((prev_point, point))
            combined.append((prev_point, point))
            prev_point = point
    return (horizontal, vertical, combined)


print(solve_day_03("test_input_0.txt"))
print(solve_day_03("test_input_1.txt"))
print(solve_day_03("test_input_2.txt"))
print(solve_day_03("input.txt"))
