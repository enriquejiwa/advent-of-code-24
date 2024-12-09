import sys
import heapq
from collections import defaultdict


def parse_input() -> str:
    return sys.stdin.readline().strip("\r\n")


def compute_disk(
    input: str,
) -> tuple[list[int], defaultdict[int, list[int]], int, list[tuple[int, int]]]:
    disk = []
    empty_spaces = defaultdict(list)
    biggest_space = 0
    index_to_size = []
    for i, value in enumerate(input):
        if i % 2:
            if not int(value):
                continue
            heapq.heappush(empty_spaces[int(value)], len(disk))
            biggest_space = max(biggest_space, int(value))
            disk += ["." for _ in range(int(value))]
        else:
            index_to_size.append((len(disk), int(value)))
            disk += [i // 2 for _ in range(int(value))]
    return disk, empty_spaces, biggest_space, index_to_size


def reorganize_disk(
    disk: list[int],
    empty_spaces: defaultdict[int, list[int]],
    biggest_space: int,
    index_to_size: list[tuple[int, int]],
):
    for index, length in reversed(index_to_size):
        min_index = len(disk)
        min_size = biggest_space
        for l in range(length, biggest_space + 1):
            if empty_spaces[l] and empty_spaces[l][0] < min_index:
                min_index = empty_spaces[l][0]
                min_size = l
        if min_index > index:
            continue
        for i in range(length):
            disk[min_index + i], disk[index + i] = disk[index + i], disk[min_index + i]
        heapq.heappop(empty_spaces[min_size])
        if min_size > length:
            heapq.heappush(empty_spaces[min_size - length], min_index + length)
    return disk


def compute_checksum(disk: list[int]):
    checksum = 0
    for i, id in enumerate(disk):
        if id == ".":
            continue
        checksum += i * id
    return checksum


def main():
    input = parse_input()
    disk = reorganize_disk(*compute_disk(input))
    print(compute_checksum(disk))


# python 02.py < input > output
if __name__ == "__main__":
    main()
