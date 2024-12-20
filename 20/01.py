import sys


class CPU:
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    shortcuts = [
        (1, -1),
        (1, 1),
        (2, 0),
        (-1, -1),
        (-1, 1),
        (0, -2),
        (0, 2),
        (-2, 0),
        (1, -1),
        (1, 1),
        (-1, -1),
        (-1, 1),
    ]
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

    def compute_shortcuts(self, at_least_saved):
        count = 0
        for node in self.path:
            for di, dj in self.shortcuts:
                ni, nj = node[0] + di, node[1] + dj
                if (
                    0 <= ni < len(self.grid)
                    and 0 <= nj < len(self.grid[0])
                    and self.grid[ni][nj] != "#"
                    and (ni, nj) in self.path
                ):
                    time_saved = self.path[(ni, nj)] - self.path[node] - 2
                    if time_saved >= at_least_saved:
                        count += 1
        print(count)


def main():
    cpu = CPU()
    cpu.solve_maze()
    cpu.compute_shortcuts(100)


# python 01.py < input > output
if __name__ == "__main__":
    main()
