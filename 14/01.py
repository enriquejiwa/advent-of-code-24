import sys
import math


def parse_input():
    return [
        [
            [int(num) for num in p.strip("p=").split(",")],
            [int(num) for num in v.strip("v=").split(",")],
        ]
        for line in sys.stdin
        for p, v in [line.split()]
    ]


map_size = (101, 103)


def move_times(p, v, t):
    return ((p[0] + v[0] * t) % map_size[0], (p[1] + v[1] * t) % map_size[1])


def main():
    robots = parse_input()
    quadrants = [0] * 4
    x_mid = map_size[0] // 2
    y_mid = map_size[1] // 2
    for robot in robots:
        p = move_times(*robot, 100)
        if p[0] < x_mid and p[1] < y_mid:
            quadrants[0] += 1
        elif p[0] > x_mid and p[1] < y_mid:
            quadrants[1] += 1
        elif p[0] > x_mid and p[1] > y_mid:
            quadrants[2] += 1
        elif p[0] < x_mid and p[1] > y_mid:
            quadrants[3] += 1
    print(math.prod(quadrants))


# python 01.py < input > output
if __name__ == "__main__":
    main()
