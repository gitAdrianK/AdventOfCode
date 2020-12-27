class IntCodeComputer:

    memory = None
    reset_memory = None
    instruction_pointer = 0
    parameter_mode = 0

    def __init__(self):
        pass

    def initialize_memory(self, input):
        self.memory = []
        self.reset_memory = []
        for nr in input:
            self.memory.append(int(nr))
            self.reset_memory.append(int(nr))

    def execute_instruction(self):
        op_code = self.memory[self.instruction_pointer]
        if op_code == 99:
            return 0
        switcher = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
        }
        func = switcher.get(op_code)
        func()

    def reset_computer(self):
        self.instruction_pointer = 0
        self.memory = self.reset_memory.copy()

    def run(self):
        while True:
            if self.execute_instruction() == 0:
                return

    def add(self):
        self.memory[self.memory[self.instruction_pointer+3]] = self.memory[self.memory[self.instruction_pointer+1]
                                                                           ] + self.memory[self.memory[self.instruction_pointer+2]]
        self.instruction_pointer += 4

    def multiply(self):
        self.memory[self.memory[self.instruction_pointer+3]] = self.memory[self.memory[self.instruction_pointer+1]
                                                                           ] * self.memory[self.memory[self.instruction_pointer+2]]
        self.instruction_pointer += 4

    def input(self):
        is_valid = False
        input_ = 0
        while not is_valid:
            input_ = input("Please enter a single integer number:")
            is_valid = input_.isdigit()
        self.memory[self.memory[self.instruction_pointer+1]] = input_
        self.instruction_pointer += 2

    def output(self):
        print(self.memory[self.memory[self.instruction_pointer+1]])
        self.instruction_pointer += 2
