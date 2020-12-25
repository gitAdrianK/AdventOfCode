def solve_day_01(input):
    p1 = 0
    p2 = 0
    f = open(input, "r")
    for mass in (int(mass) for mass in list(f.readlines())):
        fuel = int(mass/3) - 2
        p1 += fuel
        p2 += fuel
        while fuel > 0:
            fuel = int(fuel/3) - 2
            if fuel > 0:
                p2 += fuel
    return (p1, p2)


print(solve_day_01("input.txt"))
