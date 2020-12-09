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
# Part 1 answer: 50047984
l2 = list()
hasFound = False
f = open("input.txt", "r")
for line in f.readlines():
    # Part 2
    if not hasFound:
        l2.append(int(line))
        l2_sum = sum(l2)
        # Check if just adding a new number to the list gets the result
        if l2_sum == 50047984:
            print(min(l2) + max(l2))
            hasFound = True
        # If the number was too large take from the front until smaller
        while l2_sum > 50047984:
            l2.pop(0)
            l2_sum = sum(l2)
            # Check if just removing a number from the list gets the result
            if l2_sum == 50047984:
                print(min(l2) + max(l2))
                hasFound = True
    # Since the numbers grow larger the sum of consecutive numbers can
    # only contain numbers from before the part 1 result has been found.
    # That means by the time part 1 finds its result and breaks the loop
    # we will already have found a solution to part 2
    # Part 1
    if len(l) == 26:
        result = hasSum(l)
        l.pop(0)
        l.append(int(line))
        if result > 0:
            print(result)
            break
    else:
        l.append(int(line))
