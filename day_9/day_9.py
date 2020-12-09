def hasSum(numbers):
    sum = numbers[-1]
    for n in numbers[:-1]:
        for m in numbers[:-1]:
            if n == m:
                continue
            if n + m == sum:
                return -1
    return sum

l = list()
f = open("input.txt", "r")
for line in f.readlines():
    if len(l) == 26:
        result = hasSum(l)
        l.pop(0)
        l.append(int(line))
        if result > 0:
            print(result)
            break
    else:
        l.append(int(line))
