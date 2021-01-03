from enum import Enum


class Status(Enum):
    CREATED = 0,
    TERMINATED = 1,
    RUNNING = 2,
    BLOCKED = 3,


class IntCodeComputer:
    def __init__(self, input):
        self.initialize_memory(input)
        self.instruction_pointer = 0
        self.relative_base = 0
        self.status = Status.CREATED
        self.input_bus = []
        self.output_bus = []

    def initialize_memory(self, input):
        self.memory = []
        self.reset_memory = []
        for nr in input:
            self.memory.append(int(nr))
            self.reset_memory.append(int(nr))

    def execute_instruction(self):
        instruction = self.memory[self.instruction_pointer]
        if instruction == 99:
            # print("The computer stopped successfully!")
            self.status = Status.TERMINATED
            return
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
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.relative,
        }
        func = switcher.get(op_code)
        if func is not None:
            func()
        else:
            print("The computer encoutered an unknown instruction!", op_code)
            self.status = Status.TERMINATED

    def reset(self):
        self.instruction_pointer = 0
        self.relative_base = 0
        self.memory = self.reset_memory.copy()
        self.status = Status.CREATED

    def run(self):
        self.status = Status.RUNNING
        while self.status == Status.RUNNING:
            try:
                self.execute_instruction()
            except IndexError:
                self.memory.extend([0]*8)
                # FIXME: IndexErrors caused by adressing negative memory
                # cause the program to continue growing memory indefinitely
                # print("The computer stopped unexpectedly!")
                # self.status = Status.TERMINATED
                # return

    def get_modes(self, pointer, leading_zeroes):
        modes = str(self.memory[pointer])
        if len(modes) < 2:
            return "".zfill(leading_zeroes)
        else:
            return modes[:-2].zfill(leading_zeroes)

    def get_by_mode(self, mode, pointer):
        # Position mode
        if mode == "0":
            return self.memory[self.memory[pointer]]
        # Immediate mode
        elif mode == "1":
            return self.memory[pointer]
        # Relative mode
        elif mode == "2":
            return self.memory[self.memory[pointer]+self.relative_base]
        else:
            print("The computer encountered an unknown mode!", mode)
            self.status = Status.TERMINATED

    def set_by_mode(self, mode, pointer, value):
        # Position mode
        if mode == "0":
            self.memory[self.memory[pointer]] = value
        # Immediate mode
        elif mode == "1":
            self.memory[pointer] = value
        # Relative mode
        elif mode == "2":
            self.memory[self.memory[pointer]+self.relative_base] = value
        else:
            print("The computer encountered an unknown mode!", mode)
            self.status = Status.TERMINATED

    def write(self, some):
        if type(some) is int:
            self.input_bus.append(some)
        elif type(some) is list:
            if type(some[0]) is int:
                for s in some:
                    self.input_bus.append(s)

    def read(self):
        output = self.output_bus
        self.output_bus = []
        return output

    # 01
    def add(self):
        modes = self.get_modes(self.instruction_pointer, 3)
        a = self.get_by_mode(modes[2], self.instruction_pointer+1)
        b = self.get_by_mode(modes[1], self.instruction_pointer+2)
        self.set_by_mode(modes[0], self.instruction_pointer+3, a+b)
        self.instruction_pointer += 4

    # 02
    def multiply(self):
        modes = self.get_modes(self.instruction_pointer, 3)
        a = self.get_by_mode(modes[2], self.instruction_pointer+1)
        b = self.get_by_mode(modes[1], self.instruction_pointer+2)
        self.set_by_mode(modes[0], self.instruction_pointer+3, a*b)
        self.instruction_pointer += 4

    # 03
    def input(self):
        if len(self.input_bus) == 0:
            self.status = Status.BLOCKED
        else:
            modes = self.get_modes(self.instruction_pointer, 1)
            self.set_by_mode(
                modes[0], self.instruction_pointer+1, self.input_bus.pop(0))
            self.instruction_pointer += 2

    # 04
    def output(self):
        modes = self.get_modes(self.instruction_pointer, 1)
        a = self.get_by_mode(modes[0], self.instruction_pointer+1)
        self.output_bus.append(a)
        self.instruction_pointer += 2

    # 05
    def jump_if_true(self):
        modes = self.get_modes(self.instruction_pointer, 2)
        a = self.get_by_mode(modes[1], self.instruction_pointer+1)
        b = self.get_by_mode(modes[0], self.instruction_pointer+2)
        if a != 0:
            self.instruction_pointer = b
        else:
            self.instruction_pointer += 3

    # 06
    def jump_if_false(self):
        modes = self.get_modes(self.instruction_pointer, 2)
        a = self.get_by_mode(modes[1], self.instruction_pointer+1)
        b = self.get_by_mode(modes[0], self.instruction_pointer+2)
        if a == 0:
            self.instruction_pointer = b
        else:
            self.instruction_pointer += 3

    # 07
    def less_than(self):
        modes = self.get_modes(self.instruction_pointer, 3)
        a = self.get_by_mode(modes[2], self.instruction_pointer+1)
        b = self.get_by_mode(modes[1], self.instruction_pointer+2)
        if a < b:
            self.set_by_mode(modes[0], self.instruction_pointer+3, 1)
        else:
            self.set_by_mode(modes[0], self.instruction_pointer+3, 0)
        self.instruction_pointer += 4

    # 08
    def equals(self):
        modes = self.get_modes(self.instruction_pointer, 3)
        a = self.get_by_mode(modes[2], self.instruction_pointer+1)
        b = self.get_by_mode(modes[1], self.instruction_pointer+2)
        if a == b:
            self.set_by_mode(modes[0], self.instruction_pointer+3, 1)
        else:
            self.set_by_mode(modes[0], self.instruction_pointer+3, 0)
        self.instruction_pointer += 4

    # 09
    def relative(self):
        modes = self.get_modes(self.instruction_pointer, 1)
        a = self.get_by_mode(modes[0], self.instruction_pointer+1)
        self.relative_base += a
        self.instruction_pointer += 2
