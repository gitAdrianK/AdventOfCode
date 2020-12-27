from intcode_computer import IntCodeComputer
import unittest
import re


class TestStringMethods(unittest.TestCase):

    regex = re.compile("\d+")

    def test_addition(self):
        computer = IntCodeComputer(self.regex.findall("1,0,0,0,99"))
        computer.run()
        self.assertEqual([2, 0, 0, 0, 99], computer.memory)

    def test_multiplication(self):
        computer = IntCodeComputer(self.regex.findall("2,3,0,3,99"))
        computer.run()
        self.assertEqual([2, 3, 0, 6, 99], computer.memory)

    def test_large_multiplication(self):
        computer = IntCodeComputer(self.regex.findall("2,4,4,5,99,0"))
        computer.run()
        self.assertEqual([2, 4, 4, 5, 99, 9801], computer.memory)

    def test_addition_multiplication(self):
        computer = IntCodeComputer(self.regex.findall("1,1,1,4,99,5,6,0,99"))
        computer.run()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], computer.memory)

    def test_reset(self):
        computer = IntCodeComputer(self.regex.findall("1,1,1,4,99,5,6,0,99"))
        computer.run()
        computer.reset_computer()
        self.assertEqual([1, 1, 1, 4, 99, 5, 6, 0, 99], computer.memory)

    def test_modes(self):
        computer = IntCodeComputer(self.regex.findall("1002,4,3,4,33"))
        computer.run()
        self.assertEqual([1002, 4, 3, 4, 99], computer.memory)


if __name__ == '__main__':
    unittest.main()
