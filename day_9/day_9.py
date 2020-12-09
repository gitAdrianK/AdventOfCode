# One of my best function names yet
def noneIfContained(set_, sum_):
    set_ = sorted(set_)
    l, r = 0, len(set_) - 1
    while l < r:
        if (set_[l] + set_[r] == sum_):
            return
        elif (set_[l] + set_[r] < sum_):
            l += 1
        else:
            r -= 1
    return sum_

def solveDay9(input, preamble):
    # Setup
    f = open(input, "r")
    lines = list([int(l) for l in f.readlines()])
    # Part 1
    p1 = None
    p1_at = None
    for r in range(preamble, len(lines)):
        p1 = noneIfContained(lines[r - preamble:r], lines[r])
        if p1 is not None:
            p1_at = r
            break
    # Part 2
    p2 = None
    l, r = 0, 1
    while p2 is None and r < p1_at:
        sum_ = sum(lines[l:r])
        if sum_ == p1:
            p2 = min(lines[l:r]) + max(lines[l:r])
        elif sum_ < p1:
            r += 1
        else:
            l += 1
    return(p1, p2)

assert (127, 62) == solveDay9("test_input.txt", 5)
print(solveDay9("input.txt", 25))
