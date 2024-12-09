import sys


def parse_input() -> str:
    return sys.stdin.readline().strip("\r\n")


def compute_checksum(input: str):
    left, right = 0, len(input) - 1
    checksum = 0
    leftover = int(input[right])
    current_block = 0
    while left < right:
        for _ in range(int(input[left])):
            checksum += (left // 2) * current_block
            current_block += 1
        for _ in range(int(input[left + 1])):
            if not leftover:
                right -= 2
                if right <= left:
                    break
                leftover = int(input[right])
            checksum += (right // 2) * current_block
            current_block += 1
            leftover -= 1
        left += 2
    while leftover:
        checksum += (right // 2) * current_block
        current_block += 1
        leftover -= 1
    return checksum


def main():
    input = parse_input()
    print(compute_checksum(input))


# python 01.py < input > output
if __name__ == "__main__":
    main()
