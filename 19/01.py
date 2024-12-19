import sys


class HotSpring:

    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.patterns = sys.stdin.readline().strip().split(", ")
        sys.stdin.readline()
        self.designs = [line.strip() for line in sys.stdin]

    def create_design(self, design):
        if not design:
            return True
        for pattern in self.patterns:
            if len(pattern) > len(design):
                continue
            if pattern == design[: len(pattern)]:
                if self.create_design(design[len(pattern) :]):
                    return True
        return False

    def compute_designs(self):
        print(sum(self.create_design(design) for design in self.designs))


def main():
    hs = HotSpring()
    hs.compute_designs()


# python 01.py < input > output
if __name__ == "__main__":
    main()
