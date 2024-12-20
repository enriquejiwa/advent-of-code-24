import sys
from itertools import combinations


class CPU:
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    path = dict()

    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.grid = [line.strip() for line in sys.stdin]
        for row in self.grid:
            if "S" in row:
                self.start = (self.grid.index(row), row.index("S"))
            if "E" in row:
                self.end = (self.grid.index(row), row.index("E"))

    def solve_maze(self):
        node = self.start
        self.path[node] = 0
        steps = 1
        while node != self.end:
            for di, dj in self.directions:
                ni, nj = node[0] + di, node[1] + dj
                if (
                    0 <= ni < len(self.grid)
                    and 0 <= nj < len(self.grid[0])
                    and self.grid[ni][nj] != "#"
                    and (ni, nj) not in self.path
                ):
                    self.path[(ni, nj)] = steps
                    node = (ni, nj)
                    steps += 1
                    break

    def distance(self, node, target):
        return abs(node[0] - target[0]) + abs(node[1] - target[1])

    def compute_shortcuts(self, at_least_saved):
        count = 0
        for node, target in combinations(self.path.keys(), 2):
            distance = self.distance(node, target)
            if distance > 20:
                continue
            time_saved = self.path[target] - self.path[node] - distance
            if time_saved >= at_least_saved:
                count += 1
        print(count)


def main():
    cpu = CPU()
    cpu.solve_maze()
    cpu.compute_shortcuts(100)


# python 02.py < input > output
if __name__ == "__main__":
    main()
