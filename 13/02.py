import sys


def parse_input():
    state = 0
    input = []
    for line in sys.stdin:
        match state:
            case 0:
                input.append([(int(line[12:14]), int(line[18:20]))])
            case 1:
                input[-1].append((int(line[12:14]), int(line[18:20])))
            case 2:
                comma = line.index(",")
                x = int(line[9:comma])
                y = int(line[comma + 4 :].strip())
                input[-1].append((x, y))
        state = (state + 1) % 4
    return input


def compute_tokens(input: list[tuple[int, int]]):
    a_button, b_button, prize = input
    a = a_button[0]
    b = b_button[0]
    c = a_button[1]
    d = b_button[1]
    x = prize[0] + 10000000000000
    y = prize[1] + 10000000000000
    div = a * d - b * c
    return (
        (d * x - b * y) / div,
        (-c * x + a * y) / div,
    )


def main():
    input = parse_input()
    tokens = 0
    for line in input:
        a, b = compute_tokens(line)
        if a.is_integer() and b.is_integer():
            tokens += 3 * int(a) + int(b)
    print(tokens)


# python 02.py < input > output
if __name__ == "__main__":
    main()
