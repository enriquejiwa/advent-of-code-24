import sys
from collections import defaultdict

def parse_input() -> list[list[str]]:
    return [list(line.strip('\r\n')) for line in sys.stdin]

def get_start(input: list[list[str]]):
    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j

def compute_route(input: list[list[str]], start: tuple[int, int]):
    n, m = len(input), len(input[0])
    i, j = start
    visited = defaultdict(lambda: 1, {start: 2})
    dirs = [(-1, 0, 2), (0, 1, 3), (1, 0, 5), (0, -1, 7)]
    dir = 0
    is_loop = False
    while True:
        ni, nj = i + dirs[dir][0], j + dirs[dir][1]
        if not (0 <= ni < n and 0 <= nj < m):
            break
        if input[ni][nj] == '#':
            dir = (dir + 1) % 4
            continue
        if not visited[(ni, nj)] % dirs[dir][2]:
            is_loop = True
            break
        else:
            visited[(ni, nj)] *= dirs[dir][2]
        i, j = ni, nj
    return visited.keys(), is_loop

def main():
    input = parse_input()
    start = get_start(input)
    route = compute_route(input, start)[0]
    res = 0
    for pos in route:
        if pos == start:
            continue
        input[pos[0]][pos[1]] = '#'
        res += compute_route(input, start)[1]
        input[pos[0]][pos[1]] = '.'
    print(res)

# python 02.py < input > output
if __name__ == '__main__':
    main()