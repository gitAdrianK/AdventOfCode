def hasSum(numbers):
    sum = numbers[-1]
    for n in numbers[:-1]:
        for m in numbers[:-1]:
            if n == m:
                continue
            if n + m == sum:
                return -1
    return sum

# For a list as small as 25 this function is not faster
# However if we change
#   if len(l) == 26:
# to
#   if len(l) == 220:
# We can notice a speed increase
# Using cProfile:
# 26 Elements
#   hasSum      =>  3880 function calls in 0.008 seconds
#   hasSumAlt   =>  4916 function calls in 0.008 seconds
# 220 Elements
#   hasSum      =>  3492 function calls in 1.398 seconds
#   hasSumAlt   =>  4140 function calls in 0.032 seconds
def hasSumAlt(numbers):
    sum = numbers[-1]
    sorted_numbers = sorted(numbers[:-1])
    left = 0
    right = len(sorted_numbers) - 1
    while left < right:
        if (sorted_numbers[left] + sorted_numbers[right] == sum):
            return -1
        elif (sorted_numbers[left] + sorted_numbers[right] < sum):
            left += 1
        else:
            right -= 1
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
        result = hasSumAlt(l)
        l.pop(0)
        l.append(int(line))
        if result > 0:
            print(result)
            break
    else:
        l.append(int(line))
