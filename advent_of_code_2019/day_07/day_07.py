import re
import sys
from io import StringIO
from itertools import permutations
from intcode_computer import IntCodeComputer


def solve_day_06(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    p1 = 0
    computer = IntCodeComputer(regex.findall(f.readline()))
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    for perm in permutations([0, 1, 2, 3, 4]):
        new_stdout = StringIO()
        sys.stdout = new_stdout
        start = str(perm[0]) + "\n0\n"
        sys.stdin = StringIO(start)
        computer.run()
        output = re.sub("[^0-9]", "", new_stdout.getvalue())
        computer.reset()
        for p in perm[1:]:
            new_stdout = StringIO()
            sys.stdout = new_stdout
            start = str(p) + "\n" + output + "\n"
            sys.stdin = StringIO(start)
            computer.run()
            output = re.sub("[^0-9]", "", new_stdout.getvalue())
            computer.reset()
        if p1 < int(output):
            p1 = int(output)
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    return p1


print(solve_day_06("input.txt"))
