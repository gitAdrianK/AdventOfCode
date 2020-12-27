import re


def solve_day_04(input):
    regex = re.compile("\d+")
    f = open(input, "r")
    input = regex.findall(f.readline())
    start = int(input[0])
    end = int(input[1])
    p1 = 0
    p2 = 0
    for i in range(start, end+1):
        i = str(i)
        has_double = False
        has_double_p2 = False
        is_rising = True
        prev = None
        for j in range(len(i)-1):
            curr = int(i[j])
            next = int(i[j+1])
            if curr > next:
                is_rising = False
                break
            # I am convinced there could be a pretty one line regex here instead of this
            # or before we enter the loop even
            if curr == next:
                has_double = True
                if prev == curr == next:
                    has_double_p2 = False
                else:
                    if not has_double_p2:
                        prev = curr
                    has_double_p2 = True
        if is_rising and has_double:
            p1 += 1
        if is_rising and has_double_p2:
            p2 += 1

    return (p1, p2)


print(solve_day_04("test_input_0.txt"))
print(solve_day_04("test_input_1.txt"))
print(solve_day_04("test_input_2.txt"))
print(solve_day_04("test_input_3.txt"))
print(solve_day_04("test_input_4.txt"))
print(solve_day_04("test_input_5.txt"))
print(solve_day_04("input.txt"))
