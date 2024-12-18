import sys


class RAM:
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def __init__(self, size):
        self.size = size
        self.parse_input()

    def parse_input(self):
        self.corrupted = [
            (int(x), int(y)) for line in sys.stdin for x, y in [line.strip().split(",")]
        ]

    def solve_maze(self, bytes_fallen):
        print(self.corrupted[bytes_fallen])
        walls = set(self.corrupted[:bytes_fallen])
        queue = [(0, 0, 0)]
        visited = set()
        while queue:
            x, y, steps = queue.pop(0)
            if (x + 1, y + 1) == self.size:
                return print(steps)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < self.size[0]
                    and 0 <= ny < self.size[1]
                    and (nx, ny) not in walls
                ):
                    queue.append((nx, ny, steps + 1))


def main():
    ram = RAM((71, 71))
    ram.solve_maze(2994)


# python 01.py < input > output
if __name__ == "__main__":
    main()
