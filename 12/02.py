import sys


def parse_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def count_corners(visited: set[tuple[int, int]]):
    total_corners = 0
    for i, j in visited:
        for dir in range(4):
            side1 = i + directions[dir][0], j + directions[dir][1]
            side2 = i + directions[(dir + 1) % 4][0], j + directions[(dir + 1) % 4][1]
            if side1 not in visited and side2 not in visited:
                total_corners += 1
                continue
            corner = (
                i + directions[dir][0] + directions[(dir + 1) % 4][0],
                j + directions[dir][1] + directions[(dir + 1) % 4][1],
            )
            if side1 in visited and side2 in visited and corner not in visited:
                total_corners += 1
    return total_corners


def compute_region(map: list[str], i: int, j: int):
    plant = map[i][j]
    stack = [(i, j)]
    visited = set()
    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        internal_sides = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= len(map) or nj < 0 or nj >= len(map[i]):
                continue
            if (ni, nj) in visited:
                internal_sides += 1
                continue
            if map[ni][nj] == plant:
                stack.append((ni, nj))
    return len(visited) * count_corners(visited), visited


def compute_price(map: list[str]):
    visited = set()
    price = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i, j) in visited:
                continue
            region_price, region_visited = compute_region(map, i, j)
            visited |= region_visited
            price += region_price
    return price


def main():
    input = parse_input()
    print(compute_price(input))


# python 02.py < input > output
if __name__ == "__main__":
    main()
