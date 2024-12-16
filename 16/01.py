import sys
import heapq


def parse_input():
    return [list(line.strip()) for line in sys.stdin]


def navigate_maze(grid: list[list[str]]):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (len(grid) - 2, 1, 0)
    end = (1, len(grid[0]) - 2)

    queue = [(0, start)]
    visited = set()

    while queue:
        steps, (i, j, dir) = heapq.heappop(queue)
        if (i, j) == end:
            return steps
        if (i, j, dir) in visited:
            continue

        visited.add((i, j, dir))
        ni, nj = i + directions[dir][0], j + directions[dir][1]
        if grid[ni][nj] != "#":
            heapq.heappush(queue, (steps + 1, (ni, nj, dir)))
        for d in (1, -1):
            ndir = (dir + d) % 4
            if (i, j, ndir) not in visited:
                heapq.heappush(queue, (steps + 1000, (i, j, ndir)))


def main():
    grid = parse_input()
    print(navigate_maze(grid))


# python 01.py < input > output
if __name__ == "__main__":
    main()
