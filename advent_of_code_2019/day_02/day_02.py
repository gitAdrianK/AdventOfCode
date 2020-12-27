import re

from intcode_computer import IntCodeComputer
def solve_day_02(input):
    computer = IntCodeComputer()
    regex = re.compile("\d+")
    f = open(input, "r")
    computer.initialize_memory(regex.findall(f.readline()))
    computer.run()
    p1 = computer.memory[0]
    p2 = 0
    has_found = False
    for noun in range(99):
        for verb in range(99):
            computer.reset_computer()
            computer.memory[1] = noun
            computer.memory[2] = verb
            computer.run()
            if computer.memory[0] == 19690720:
                p2 = 100 * noun + verb
                has_found = True
                break
        if has_found:
            break
    return (p1, p2)

print(solve_day_02("input.txt"))
