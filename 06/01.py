import sys
from collections import defaultdict

def parse_input() -> list[list[str]]:
    return [list(line.strip('\r\n')) for line in sys.stdin]

def get_start(input: list[list[str]]):
    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j

def main():
    input = parse_input()
    n, m = len(input), len(input[0])
    i, j = get_start(input)
    visited = 1
    input[i][j] = 'X'
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0
    while True:
        ni, nj = i + dirs[dir][0], j + dirs[dir][1]
        if not (0 <= ni < n and 0 <= nj < m):
            break
        if input[ni][nj] == '.':
            visited += 1
            input[ni][nj] = 'X'
            i, j = ni, nj
        elif input[ni][nj] == '#':
            dir = (dir + 1) % 4
        else:
            i, j = ni, nj
    print(visited)

# python 01.py < input > output
if __name__ == '__main__':
    main()