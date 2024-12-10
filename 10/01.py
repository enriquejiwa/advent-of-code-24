import sys


def parse_input():
    return [[int(height) for height in line.strip()] for line in sys.stdin]


def compute_trailhead_score_helper(
    map: list[list[int]], i: int, j: int, v: int, tops: set
):
    if v == 10:
        tops.add((i, j))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(map) and 0 <= nj < len(map[ni]) and map[ni][nj] == v:
            compute_trailhead_score_helper(map, ni, nj, v + 1, tops)


def compute_trailhead_score(map: list[list[int]], i: int, j: int):
    tops = set()
    compute_trailhead_score_helper(map, i, j, 1, tops)
    return len(tops)


def compute_scores(map: list[list[int]]):
    score = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                score += compute_trailhead_score(map, i, j)
    return score


def main():
    input = parse_input()
    print(compute_scores(input))


# python 01.py < input > output
if __name__ == "__main__":
    main()
