import sys


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


def draw_map(robots):
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if (x, y) in robots:
                print("X", end="")
            else:
                print(".", end="")
        print()


def main():
    robots = parse_input()
    quadrants = [0] * 4
    x_mid = map_size[0] // 2
    y_mid = map_size[1] // 2
    best = 0
    outliers = []
    for iteration in range(10000):
        for i in range(len(robots)):
            robots[i][0] = p = move_times(*robots[i], 1)
            if p[0] < x_mid and p[1] < y_mid:
                quadrants[0] += 1
            elif p[0] > x_mid and p[1] < y_mid:
                quadrants[1] += 1
            elif p[0] > x_mid and p[1] > y_mid:
                quadrants[2] += 1
            elif p[0] < x_mid and p[1] > y_mid:
                quadrants[3] += 1
        if max(quadrants) > best:
            best = max(quadrants)
            outliers.append((iteration, [robot[0] for robot in robots]))
        quadrants = [0] * 4
    for iteration, map in outliers:
        print(iteration + 1)
        draw_map(map)


# python 02.py < input > output
if __name__ == "__main__":
    main()
