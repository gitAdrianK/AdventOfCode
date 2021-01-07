def solve_day_16(input):
    pattern = [0, 1, 0, -1]
    f = open(input, "r")
    input = [int(c) for c in list(f.readline().replace("\n", ""))]
    #input *= 10_000
    output = [0]*len(input)
    for _ in range(100):
        for i in range(len(input)):
            new = 0
            for j, k in enumerate(input[i:], i+1):
                new += pattern[int(j/(i+1)) % len(pattern)]*k
            output[i] = abs(new) % 10
        input = output
    p1 = int("".join(str(nr) for nr in output[:8]))
    return (p1, input[p1:p1+8])


print(solve_day_16("test_input_0.txt"))
print(solve_day_16("test_input_1.txt"))
print(solve_day_16("test_input_2.txt"))
print(solve_day_16("input.txt"))
