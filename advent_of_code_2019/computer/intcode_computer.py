class IntCodeComputer:

    memory = None
    reset_memory = None
    instruction_pointer = 0

    def __init__(self, input):
        self.initialize_memory(input)

    def initialize_memory(self, input):
        self.memory = []
        self.reset_memory = []
        for nr in input:
            self.memory.append(int(nr))
            self.reset_memory.append(int(nr))

    def execute_instruction(self):
        instruction = self.memory[self.instruction_pointer]
        if instruction == 99:
            return 0
        op_code = None
        instruction_str = str(instruction)
        if len(instruction_str) > 2:
            op_code = int(instruction_str[-2:])
        else:
            op_code = int(instruction_str)
        switcher = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
        }
        func = switcher.get(op_code)
        try:
            func()
        except TypeError:
            return op_code

    def reset_computer(self):
        self.instruction_pointer = 0
        self.memory = self.reset_memory.copy()

    def run(self):
        while True:
            try:
                exit_code = self.execute_instruction()
                if exit_code is not None:
                    if exit_code == 0:
                        #print("The computer stopped successfully!")
                        return
                    else:
                        print("The computer encoutered an unknown instruction!", exit_code)
                        return
            except IndexError:
                print("The computer stopped unexpectedly!")
                return

    def get_modes(self, pointer, leading_zeroes):
        modes = str(self.memory[pointer])
        if len(modes) < 2:
            return "".zfill(leading_zeroes)
        else:
            return modes[:-2].zfill(leading_zeroes)

    def get_by_mode(self, mode, pointer):
        if mode == "0":
            return self.memory[self.memory[pointer]]
        else:
            return self.memory[pointer]

    def add(self):
        modes = self.get_modes(self.instruction_pointer, 2)
        A = self.get_by_mode(modes[1], self.instruction_pointer+1)
        B = self.get_by_mode(modes[0], self.instruction_pointer+2)
        self.memory[self.memory[self.instruction_pointer+3]] = A+B
        self.instruction_pointer += 4

    def multiply(self):
        modes = self.get_modes(self.instruction_pointer, 2)
        A = self.get_by_mode(modes[1], self.instruction_pointer+1)
        B = self.get_by_mode(modes[0], self.instruction_pointer+2)
        self.memory[self.memory[self.instruction_pointer+3]] = A*B
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
