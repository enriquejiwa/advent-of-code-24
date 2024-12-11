import sys


def parse_input():
    return [int(num) for num in sys.stdin.readline().strip().split(" ")]


memo = dict()


def compute_stones(number: int, blinks: int):
    if blinks == 0:
        return 1

    if (number, blinks) in memo:
        return memo[(number, blinks)]

    stones = 0
    if number == 0:
        stones = compute_stones(1, blinks - 1)
    elif not len(str(number)) % 2:
        number_str = str(number)
        mid = len(number_str) // 2
        stones = compute_stones(int(number_str[:mid]), blinks - 1) + compute_stones(
            int(number_str[mid:]), blinks - 1
        )
    else:
        stones = compute_stones(2024 * number, blinks - 1)

    memo[(number, blinks)] = stones
    return stones


def compute_line(input: list[int], blinks: int):
    return sum(compute_stones(number, blinks) for number in input)


def main():
    input = parse_input()
    print(compute_line(input, 75))


# python 02.py < input > output
if __name__ == "__main__":
    main()
