import sys
import re

def parse_input():
    return sys.stdin.read()

def main():
    input = parse_input()
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)
    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])
    print(res)

# 30632041 too low

# python 01.py < input > output
if __name__ == '__main__':
    main()