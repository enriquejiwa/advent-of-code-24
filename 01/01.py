import sys

def parse_input() -> tuple[list[int], list[int]]:
    lines =  [_.strip('\r\n').split('   ') for _ in sys.stdin]
    return map(list, zip(*lines))

def main():
    left, right = parse_input()
    left.sort()
    right.sort()
    count = 0
    for l, r in zip(left, right):
        count += abs(int(l) - int(r))
    print(count)

# python 01.py < input > output
if __name__ == '__main__':
    main()