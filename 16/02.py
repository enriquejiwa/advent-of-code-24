import sys
import heapq
import math
from collections import defaultdict


def parse_input():
    return [list(line.strip()) for line in sys.stdin]


def backtrack(end, grid_prev):
    path = set()
    stack = [end]
    while stack:
        curr = stack.pop()
        path.add(curr[:2])
        stack.extend(grid_prev[curr][1])
    return path


def add_to_grid_prev(grid_prev, steps, curr, prev):
    if steps < grid_prev[curr][0]:
        grid_prev[curr] = (steps, [prev])
    elif steps == grid_prev[curr][0]:
        grid_prev[curr][1].append(prev)


def navigate_maze(grid: list[list[str]]):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (len(grid) - 2, 1, 0)
    end = (1, len(grid[0]) - 2)

    queue = [(0, start)]
    visited = set()

    grid_prev = defaultdict(lambda: (math.inf, []))

    while queue:
        steps, (i, j, dir) = heapq.heappop(queue)
        if (i, j) == end:
            path = backtrack((i, j, dir), grid_prev)
            return len(path)
        if (i, j, dir) in visited:
            continue

        visited.add((i, j, dir))
        ni, nj = i + directions[dir][0], j + directions[dir][1]
        if grid[ni][nj] != "#":
            heapq.heappush(queue, (steps + 1, (ni, nj, dir)))
            add_to_grid_prev(grid_prev, steps + 1, (ni, nj, dir), (i, j, dir))
        for d in (1, -1):
            ndir = (dir + d) % 4
            if (i, j, ndir) not in visited:
                heapq.heappush(queue, (steps + 1000, (i, j, ndir)))
                add_to_grid_prev(grid_prev, steps + 1000, (i, j, ndir), (i, j, dir))


def main():
    grid = parse_input()
    print(navigate_maze(grid))


# python 02.py < input > output
if __name__ == "__main__":
    main()
