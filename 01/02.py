import sys
import collections

def parse_input() -> tuple[list[int], list[int]]:
    lines =  [_.strip('\r\n').split('   ') for _ in sys.stdin]
    return map(list, zip(*lines))

def main():
    left, right = parse_input()
    counts = collections.Counter(right)
    count = 0
    for l in left:
        count += int(l) * counts[l]
    print(count)

# python 01.py < input > output
if __name__ == '__main__':
    main()