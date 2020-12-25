import re


class IntCodeComputer:

    memory = []
    reset_memory = []
    instruction_pointer = None

    def __init__(self) -> None:
        self.memory = []
        self.instruction_pointer = 0

    def initialize_memory(self, input):
        regex = re.compile("\d+")
        f = open(input, "r")
        for nr in regex.findall(f.readline()):
            self.memory.append(int(nr))
            self.reset_memory.append(int(nr))

    def execute_instruction(self):
        op_code = self.memory[self.instruction_pointer]
        if op_code == 99:
            return 0
        elif op_code == 1:
            self.memory[self.memory[self.instruction_pointer+3]] = self.memory[self.memory[self.instruction_pointer+1]
                                                                               ] + self.memory[self.memory[self.instruction_pointer+2]]
        elif op_code == 2:
            self.memory[self.memory[self.instruction_pointer+3]] = self.memory[self.memory[self.instruction_pointer+1]
                                                                               ] * self.memory[self.memory[self.instruction_pointer+2]]
        self.instruction_pointer += 4

    def reset_computer(self):
        self.instruction_pointer = 0
        self.memory = self.reset_memory.copy()

    def run(self):
        while True:
            if self.execute_instruction() == 0:
                return
