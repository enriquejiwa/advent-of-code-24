import sys


def parse_input():
    return [
        [int(result), [int(value) for value in values.split()]]
        for line in sys.stdin
        for result, values in [line.strip("\r\n").split(": ")]
    ]


def check_equation(result: int, values: list[int], current: int, index: int):
    if current > result:
        return False
    if index == len(values):
        return current == result
    return check_equation(
        result, values, current * values[index], index + 1
    ) or check_equation(result, values, current + values[index], index + 1)


def main():
    input = parse_input()
    res = 0
    for result, values in input:
        if check_equation(result, values, values[0], 1):
            res += result
    print(res)


# python 01.py < input > output
if __name__ == "__main__":
    main()
