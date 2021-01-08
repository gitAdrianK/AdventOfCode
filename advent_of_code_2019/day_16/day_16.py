def solve_day_16(input):
    pattern = [0, 1, 0, -1]
    pattern_length = 4
    f = open(input, "r")
    input = [int(c) for c in list(f.readline().replace("\n", ""))]
    #input *= 10_000     # Disable for p1 result
    length = len(input)
    half = length//2
    third = length//3
    output = [0]*length
    for _ in range(100):
        output[-1] = input[-1]
        for i in range(length-2, -1, -1):
            if i >= half:
                output[i] = (input[i]+output[i+1]) % 10
            elif i >= third:
                try:
                    output[i] = input[i]+output[i+1]-input[i+i+1]-input[i+i+2]
                except IndexError:
                    output[i] = input[i]+output[i+1]-input[i+i+1]
                output[i] = output[i] % 10
            else:
                new = 0
                for j, k in enumerate(input[i:], i+1):
                    new += pattern[j//(i+1) % pattern_length]*k
                output[i] = abs(new) % 10
        input = output
        output = [0]*length
    p1 = "".join(str(nr) for nr in input[:8])
    p2 = "".join(str(nr) for nr in input[int(p1):int(p1)+8])
    return (p1, p2)


print(solve_day_16("test_input_0.txt"))
# print(solve_day_16("test_input_1.txt"))
# print(solve_day_16("test_input_2.txt"))
print(solve_day_16("input.txt"))
