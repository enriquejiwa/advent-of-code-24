import sys


def parse_input():
    return [int(num) for num in sys.stdin.readline().strip().split(" ")]


def blink_single(number: int):
    if number == 0:
        return [1]
    number_str = str(number)
    number_digits = len(number_str)
    if not number_digits % 2:
        return [
            int(number_str[: number_digits // 2]),
            int(number_str[number_digits // 2 :]),
        ]
    return [2024 * number]


def blink_times(input: list[int], times: int):
    stones = 0
    for number in input:
        line = [number]
        for _ in range(times):
            new_line = []
            for number in line:
                new_line += blink_single(number)
            line = new_line
        stones += len(line)
    return stones


def main():
    input = parse_input()
    print(blink_times(input, 25))


# python 01.py < input > output
if __name__ == "__main__":
    main()
