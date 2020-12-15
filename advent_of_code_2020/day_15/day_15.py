def solveDay15(input):
    # Setup
    f = open(input, "r")
    start = list([int(i) for i in f.readline().split(",")])
    # Part 1
    p1 = doRambunctiousRecitation(start, 2020)
    # Part 2
    p2 = doRambunctiousRecitation(start, 30000000)

    return (p1, p2)

def doRambunctiousRecitation(start, until):
    # Start sequence
    to_say = 0
    dict = {}
    for i, j in enumerate(start):
        dict[j] = i + 1
        to_say = j
    # Play until until + 1 (range is exclusive)
    for i in range(len(start) + 1, until + 1):
        if to_say in dict:
            if dict[to_say] == i - 1:
                to_say = 0
            else:
                tmp = dict[to_say]
                dict[to_say] = i - 1
                to_say = i - 1 - tmp
        else:
            dict[to_say] = i - 1
            to_say = 0
    return to_say

#assert((436, 175594) == solveDay15("test_input_1.txt"))
#assert((1, 2578) == solveDay15("test_input.txt"))
#assert((10, 3544142) == solveDay15("test_input_2.txt"))
#assert((27, 261214) == solveDay15("test_input_3.txt"))
#assert((78, 6895259) == solveDay15("test_input_4.txt"))
#assert((438, 18) == solveDay15("test_input_5.txt"))
#assert((1836, 362) == solveDay15("test_input_6.txt"))
print(solveDay15("input.txt"))
