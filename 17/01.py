import sys


class Computer:

    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.A = int(sys.stdin.readline().strip()[12:])
        self.B = int(sys.stdin.readline().strip()[12:])
        self.C = int(sys.stdin.readline().strip()[12:])

        sys.stdin.readline()
        self.program = [int(x) for x in sys.stdin.readline().strip()[9:].split(",")]

    def get_combo_operand(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C

    def exec_instruction(self, opcode, operand):
        match opcode:
            case 0:
                self.A = self.A // 2 ** self.get_combo_operand(operand)
            case 1:
                self.B = self.B ^ operand
            case 2:
                self.B = self.get_combo_operand(operand) % 8
            case 3:
                if self.A:
                    return None, operand
            case 4:
                self.B = self.B ^ self.C
            case 5:
                return self.get_combo_operand(operand) % 8, None
            case 6:
                self.B = self.A // 2 ** self.get_combo_operand(operand)
            case 7:
                self.C = self.A // 2 ** self.get_combo_operand(operand)
        return None, None

    def run_program(self):
        i = 0
        outputs = []
        while i < len(self.program):
            opcode = self.program[i]
            operand = self.program[i + 1]
            i += 2
            output, jump = self.exec_instruction(opcode, operand)
            if output is not None:
                outputs.append(output)
            if jump is not None:
                i = jump
        print(",".join(str(num) for num in outputs))


def main():
    computer = Computer()
    computer.run_program()


# python 01.py < input > output
if __name__ == "__main__":
    main()
