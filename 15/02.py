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
            current = []
            for c in line.strip():
                if c == "#":
                    current.extend(["#", "#"])
                elif c == "O":
                    current.extend(["[", "]"])
                elif c == "@":
                    current.extend(["@", "."])
                    robot = len(grid), len(current) - 2
                else:
                    current.extend([".", "."])
            grid.append(current)
    return grid, movements, robot


mov_to_dir = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def actually_move_box(grid: list[list[str]], box: tuple[int, int], d: tuple[int, int]):
    i, j = box
    ni, nj = i + d[0], j + d[1]
    p = 1 if grid[i][j] == "[" else -1
    grid[ni][nj] = grid[i][j]
    grid[ni][nj + p] = grid[i][j + p]
    grid[i][j] = "."
    grid[i][j + p] = "."


boxes_to_move = set()


def move_box(grid: list[list[str]], box: tuple[int, int], d: tuple[int, int]):
    i, j = box
    di, dj = d
    if dj:
        ni, nj = i + 2 * di, j + 2 * dj
        c = grid[ni][nj]
        if c in "[]":
            if move_box(grid, (ni, nj), d):
                grid[ni][nj] = grid[i + di][j + dj]
                grid[i + di][j + dj] = grid[i][j]
                grid[i][j] = "."
                return True
            return False
        elif c == "#":
            return False
        else:
            grid[ni][nj] = grid[i + di][j + dj]
            grid[i + di][j + dj] = grid[i][j]
            grid[i][j] = "."
            return True
    else:
        global boxes_to_move
        ni, nj = i + di, j + dj
        p = 1 if grid[i][j] == "[" else -1
        c1 = grid[ni][nj]
        c2 = grid[ni][nj + p]
        if c1 == "#" or c2 == "#":
            return False
        if c1 in "[]" or c2 in "[]":
            moved = True
            if c1 in "[]":
                moved &= move_box(grid, (ni, nj), d)
            if c1 != grid[i][j] and c2 in "[]":
                moved &= move_box(grid, (ni, nj + p), d)
            if not moved:
                return False
        boxes_to_move.add((i, j if grid[i][j] == "[" else j + p))
        return True


def move_robot(grid: list[list[str]], robot: tuple[int, int], movement: list[str]):
    di, dj = mov_to_dir[movement]
    ni, nj = robot[0] + di, robot[1] + dj
    c = grid[ni][nj]
    if c == "#":
        return robot
    elif c in "[]":
        global boxes_to_move
        boxes_to_move = set()
        if move_box(grid, (ni, nj), (di, dj)):
            for box in sorted(list(boxes_to_move), key=lambda x: x[0], reverse=di == 1):
                actually_move_box(grid, box, (di, dj))
            grid[ni][nj] = "@"
            grid[robot[0]][robot[1]] = "."
            return ni, nj
        return robot
    else:
        grid[ni][nj] = "@"
        grid[robot[0]][robot[1]] = "."
        return ni, nj


def sum_gps(grid: list[list[str]]):
    sum = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "[":
                sum += 100 * i + j
    return sum


def main():
    grid, movements, robot = parse_input()
    for movement in movements:
        robot = move_robot(grid, robot, movement)
    print(sum_gps(grid))


# python 02.py < input > output
if __name__ == "__main__":
    main()
