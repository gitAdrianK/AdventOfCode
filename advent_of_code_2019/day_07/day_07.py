import re
from itertools import permutations
from intcode_computer import IntCodeComputer, Status


def solve_day_07(input):
    regex = re.compile("-{0,1}\d+")
    f = open(input, "r")
    intcode = regex.findall(f.readline())
    return (part_1(intcode), part_2(intcode))


def part_1(intcode):
    p1 = 0
    computer = IntCodeComputer(intcode)
    for perm in permutations([0, 1, 2, 3, 4]):
        computer.write([perm[0], 0])
        computer.run()
        output = computer.read()[0]
        computer.reset()
        for p in perm[1:]:
            computer.write([p, output])
            computer.run()
            output = computer.read()[0]
            computer.reset()
        if p1 < output:
            p1 = output
    return p1


def part_2(intcode):
    p2 = 0
    amp_a = IntCodeComputer(intcode)
    amp_b = IntCodeComputer(intcode)
    amp_c = IntCodeComputer(intcode)
    amp_d = IntCodeComputer(intcode)
    amp_e = IntCodeComputer(intcode)
    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]
    for perm in permutations([5, 6, 7, 8, 9]):
        # Setup the amps phase settings
        for amp in amps:
            amp.reset()
        for index, amp in enumerate(amps):
            amp.write(perm[index])
            amp.run()
        amp_a.write(0)
        amp_a.run()
        curr_amp = 1
        output = amp_a.read()[0]
        while amp_e.status != Status.TERMINATED:
            amps[curr_amp].write(output)
            amps[curr_amp].run()
            output = amps[curr_amp].read()[0]
            curr_amp = ((curr_amp+1) % len(amps))
        if p2 < int(output):
            p2 = int(output)
    return p2


print(solve_day_07("input.txt"))
