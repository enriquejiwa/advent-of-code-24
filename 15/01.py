import sys


def parse_input():
    map_complete = False
    grid = []
    movements = []
    robot = None
    for line in sys.stdin:
        if not line.strip():
            map_complete = True
            continue
        if map_complete:
            movements.extend(list(line.strip()))
        else:
            grid.append(list(line.strip()))
            if "@" in line:
                robot = len(grid) - 1, line.index("@")
    return grid, movements, robot


mov_to_dir = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def move_box(grid: list[list[str]], box: tuple[int, int], d: tuple[int, int]):
    i, j = box
    ni, nj = i + d[0], j + d[1]
    match grid[ni][nj]:
        case "#":
            return False
        case "O":
            if move_box(grid, (ni, nj), d):
                grid[ni][nj] = "O"
                grid[i][j] = "."
                return True
            return False
        case _:
            grid[ni][nj] = "O"
            grid[i][j] = "."
            return True


def move_robot(grid: list[list[str]], robot: tuple[int, int], movement: list[str]):
    di, dj = mov_to_dir[movement]
    ni, nj = robot[0] + di, robot[1] + dj
    match grid[ni][nj]:
        case "#":
            return robot
        case "O":
            if move_box(grid, (ni, nj), (di, dj)):
                return ni, nj
            return robot
        case _:
            return ni, nj


def sum_gps(grid: list[list[str]]):
    sum = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "O":
                sum += 100 * i + j
    return sum


def main():
    grid, movements, robot = parse_input()
    for movement in movements:
        robot = move_robot(grid, robot, movement)
    print(sum_gps(grid))


# python 01.py < input > output
if __name__ == "__main__":
    main()
