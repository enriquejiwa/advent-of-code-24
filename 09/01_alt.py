import sys


def parse_input() -> str:
    return sys.stdin.readline().strip("\r\n")


def compute_disk(input: str):
    disk = []
    for i, value in enumerate(input):
        for _ in range(int(value)):
            disk.append("." if i % 2 else i // 2)
    return disk


def reorganize_disk(disk: list[int]):
    right = len(disk) - 1
    for i, id in enumerate(disk):
        if id != ".":
            continue
        while right > i and disk[right] == ".":
            right -= 1
        disk[i], disk[right] = disk[right], disk[i]
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
    disk = compute_disk(input)
    disk = reorganize_disk(disk)
    print(compute_checksum(disk))


# python 01_alt.py < input > output
if __name__ == "__main__":
    main()
