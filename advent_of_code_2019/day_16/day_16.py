def solve_day_16(input):
    pattern = [0, 1, 0, -1]
    f = open(input, "r")
    input = [int(c) for c in list(f.readline().replace("\n", ""))]
    output = [0]*len(input)
    for _ in range(100):
        for i in range(len(input)):
            p = [nr for slst in [[pt]*(i+1) for pt in pattern] for nr in slst]
            new = 0
            for j, k in enumerate(input, 1):
                new += (p[j % len(p)])*k
            output[i] = int(list(str(new))[-1])
        input = output
    return ("".join(str(nr) for nr in output[:8]), 0)


# print(solve_day_16("test_input_0.txt"))
# print(solve_day_16("test_input_1.txt"))
# print(solve_day_16("test_input_2.txt"))
print(solve_day_16("input.txt"))
