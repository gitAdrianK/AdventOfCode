def solveDay18(input):
    # Setup
    f = open(input, "r")
    # Part 1
    p1 = 0
    p2 = 0
    for line in list(f.readlines()):
        equation = line.replace("\n", "").split(" ")
        group = bracketsToGroups(equation)
        p1 += doPart1(group)
        p2 += doPart2(group)

    return (p1, p2)

# I should just parse the input make and make a cute AST, and it would be so easy
# but noooo, "I already did that once for uni, lets do it w/o all that jazz"
def bracketsToGroups(equation):
    group = []
    sub_group = []
    bracket = 0
    for eq in equation:
        if "(" in eq:
            for c in list(eq):
                if c == "(":
                    bracket += 1
        if ")" in eq:
            for c in list(eq):
                if c == ")":
                    bracket -= 1
        if bracket == 0:
            if len(sub_group) != 0:
                sub_group.append(eq)
                group.append(sub_group)
                sub_group = []
            else:
                group.append(eq)
        else:
            sub_group.append(eq)
    finalGroup = []
    for element in group:
        if len(element) == 1:
            finalGroup.append(element)
        else:
            element[0] = element[0][1:]
            element[-1] = element[-1][:-1]
            finalGroup.append(bracketsToGroups(element))
    return finalGroup

def doPart1(expression):
    # Start
    result = expression[0]
    if len(result) != 1:
        result = str(doPart1(result))
    # Left to right evaluation
    for n, exp in enumerate(expression[1:], 1):
        # If we find an operand add the right side to result
        if len(exp) == 1:
            if "+" in exp or "*" in exp:
                next_ = expression[n + 1]
                if len(next_) == 1:
                    result = str(eval(result + exp + next_))
                else:
                    result = str(eval(result + exp + str(doPart1(next_))))
    return int(result)

def doPart2(expression):
    # Start
    left = []
    right = []
    result = expression[0]
    if len(result) != 1:
        result = str(doPart2(result))
    # Find "*" and place in left and right
    foundMult = False
    for exp in expression:
        if len(exp) == 1:
            if "*" in exp and not foundMult:
                foundMult = True
                continue
            if foundMult:
                right.append(exp)
            else:
                left.append(exp)
        else:
            if foundMult:
                right.append(str(doPart2(exp)))
            else:
                left.append(str(doPart2(exp)))
    if not foundMult:
        leftStr = ""
        for l in left:
            leftStr += l
        result = str(eval(leftStr))
    else:
        result = str(eval(str(doPart2(left)) + "*" + str(doPart2(right))))
    return int(result)

assert((26, 46) == solveDay18("test_input.txt"))
assert((437, 1445) == solveDay18("test_input_2.txt"))
assert((12240, 669060) == solveDay18("test_input_3.txt"))
assert((13632, 23340) == solveDay18("test_input_4.txt"))
print(solveDay18("input.txt"))
