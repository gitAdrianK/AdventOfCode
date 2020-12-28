import intcode_computer as ic
import re
import sys
from io import StringIO
from itertools import permutations


def solve_day_06(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    intcode = regex.findall(f.readline())
    return (part_1(intcode), part_2(intcode))


def part_1(intcode):
    p1 = 0
    computer = ic.IntCodeComputer(intcode)
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    for perm in permutations([0, 1, 2, 3, 4]):
        # Reset stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        # Ready stdin
        start = str(perm[0]) + "\n0\n"
        sys.stdin = StringIO(start)
        computer.run()
        # Get output nr
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


def part_2(intcode):
    p2 = 0
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    amp_a = ic.IntCodeComputer(intcode)
    amp_b = ic.IntCodeComputer(intcode)
    amp_c = ic.IntCodeComputer(intcode)
    amp_d = ic.IntCodeComputer(intcode)
    amp_e = ic.IntCodeComputer(intcode)
    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]
    for perm in permutations([5, 6, 7, 8, 9]):
        # Setup the amps phase settings
        for amp in amps:
            amp.reset()
        sys.stdout = StringIO()
        for index, amp in enumerate(amps):
            start = str(perm[index]) + "\npause"
            sys.stdin = StringIO(start)
            amp.run()
        new_stdout = StringIO()
        sys.stdout = new_stdout
        start = "0\npause"
        sys.stdin = StringIO(start)
        amp_a.run()
        prev_amp = 0
        curr_amp = 1
        output = re.sub("[^0-9]", "", new_stdout.getvalue())
        while amp_e.status != ic.Status.TERMINATED:
            new_stdout = StringIO()
            sys.stdout = new_stdout
            if amps[prev_amp].status == ic.Status.TERMINATED:
                start = output
            else:
                start = output + "\npause"
            sys.stdin = StringIO(start)
            amps[curr_amp].run()
            output = re.sub("[^0-9]", "", new_stdout.getvalue())
            prev_amp = curr_amp
            curr_amp = ((curr_amp+1) % len(amps))
        if p2 < int(output):
            p2 = int(output)
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    return p2


print(solve_day_06("input.txt"))
