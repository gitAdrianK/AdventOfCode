def solve_day_16(input):
    f = open(input, "r")
    input = [int(c) for c in list(f.readline().replace("\n", ""))]
    input *= 10_000     # Disable for p1 result
    length = len(input)
    output = [0]*length
    for _ in range(100):
        subsetsums = []
        do_step(input, output, subsetsums, length)
        input = output.copy()
    p1 = int("".join(str(nr) for nr in input[:8]))
    p2 = "".join(str(nr) for nr in input[p1:p1+8])
    return (p1, p2)


def do_step(input, output, subsetsums, length):
    do_first_row(input, output, subsetsums, length)
    for i in range(2, length+1):
        do_further_rows(input, output, subsetsums, length, i)


def do_first_row(input, output, subsetsums, length):
    should_add = True
    result = 0
    for pos in range(0, length, 2):
        tmp = input[pos]
        subsetsums.append((tmp, 0))
        if should_add:
            result += tmp
        else:
            result -= tmp
        should_add = not should_add
    output[0] = abs(result) % 10


def do_further_rows(input, output, subsetsums, length, i):
    should_add = True
    result = 0
    pos = i-1
    sss_nr = 0
    for pos in range(i-1, length, 2*i):
        if 1+2*sss_nr < i:
            step = sss_nr*2+2
            curr, skip = subsetsums[sss_nr]
            add = input[pos+skip:pos+skip+step]
            sub = input[pos-step+1:pos]
            subsetsums[sss_nr] = (curr+sum(add)-sum(sub), skip+1)
        else:
            subsetsums[sss_nr] = (sum(input[pos:pos+i]), 0)
        if should_add:
            result += subsetsums[sss_nr][0]
        else:
            result -= subsetsums[sss_nr][0]
        should_add = not should_add
        sss_nr += 1
    output[i-1] = abs(result) % 10


print(solve_day_16("test_input_0.txt"))
#print(solve_day_16("test_input_1.txt"))
#print(solve_day_16("test_input_2.txt"))
#print(solve_day_16("input.txt"))
