import sys


def parse_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def compute_region(map: list[str], i: int, j: int):
    plant = map[i][j]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [(i, j)]
    visited = set()
    perimeter = 0
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
        perimeter += 4 - 2 * internal_sides
    return len(visited) * perimeter, visited


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


# python 01.py < input > output
if __name__ == "__main__":
    main()
