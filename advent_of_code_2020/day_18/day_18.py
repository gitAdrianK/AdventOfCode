from os import closerange


def solveDay18(input):
    # Setup
    f = open(input, "r")
    # Part 1
    p1 = 0
    for line in list(f.readlines()):
        equation = line.replace("\n", "").split(" ")
        group = bracketsToGroups(equation)
        p1 += doMath(group)

    return (p1, 0)


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


def doMath(expression):
    result = expression[0]
    if len(result) != 1:
        result = str(doMath(result))
    for n, exp in enumerate(expression[1:], 1):
        if len(exp) == 1:
            if "+" in exp[0] or "*" in exp[0]:
                next_ = expression[n + 1]
                if len(next_) == 1:
                    result = str(eval(result + exp + next_))
                else:
                    result = str(eval(result + exp + str(doMath(next_))))
    return int(result)


assert((26, 0) == solveDay18("test_input.txt"))
assert((437, 0) == solveDay18("test_input_2.txt"))
assert((12240, 0) == solveDay18("test_input_3.txt"))
assert((13632, 0) == solveDay18("test_input_4.txt"))
print(solveDay18("input.txt"))
