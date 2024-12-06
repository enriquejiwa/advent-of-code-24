import sys

def parse_input():
    return [[int(num) for num in _.strip('\r\n').split(' ')] for _ in sys.stdin]

def check_line(line: list):
    increasing = True
    if line[1] < line[0]:
        increasing = False
    for i in range(1, len(line)):
        diff = line[i] - line[i-1]
        if increasing and not (0 < diff < 4):
            return False
        elif not increasing and not (-4 < diff < 0):
            return False
    return True

def main():
    lines = parse_input()
    count = 0
    for line in lines:
        count += check_line(line) or any(check_line(line[:i] + line[i+1:]) for i in range(len(line)))
    print(count)

# 347 too low

# python 02.py < input > output
if __name__ == '__main__':
    main()