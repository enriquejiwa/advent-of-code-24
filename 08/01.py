import sys
from collections import defaultdict
from itertools import combinations


def parse_input() -> list[str]:
    return [line.strip("\r\n") for line in sys.stdin]


def find_antennas(input: list[str]):
    antennas = defaultdict(list)
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != ".":
                antennas[input[i][j]].append((i, j))
    return antennas


def compute_antinodes(
    antennas: defaultdict[str, list[tuple[int, int]]], size: tuple[int, int]
):
    antinodes = set()
    for nodes in antennas.values():
        for node1, node2 in combinations(nodes, 2):
            di, dj = node2[0] - node1[0], node2[1] - node1[1]
            anti1 = (node1[0] - di, node1[1] - dj)
            anti2 = (node2[0] + di, node2[1] + dj)
            for anti in anti1, anti2:
                if 0 <= anti[0] < size[0] and 0 <= anti[1] < size[1]:
                    antinodes.add(anti)
    return len(antinodes)


def main():
    input = parse_input()
    antennas = find_antennas(input)
    print(compute_antinodes(antennas, (len(input), len(input[0]))))


# python 01.py < input > output
if __name__ == "__main__":
    main()
