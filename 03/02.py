import sys
import re

def parse_input():
    return sys.stdin.read()

def main():
    input = parse_input()
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', input)
    res = 0
    enabled = True
    for match in matches:
        if match[2] == "do()":
            enabled = True
        elif match[3] == "don't()":
            enabled = False
        elif enabled:
            res += int(match[0]) * int(match[1])
    print(res)

# python 02.py < input > output
if __name__ == '__main__':
    main()