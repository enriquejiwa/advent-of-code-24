import sys

def parse_input():
    return [line.strip('\r\n') for line in sys.stdin]

def check_word(input: list[str], i: int, j: int):
    word = "XMAS"
    if input[i][j] != word[0]:
        return 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for di, dj in dirs:
        full_word = True
        ni, nj = i, j
        for char in word[1:]:
            ni, nj = ni + di, nj + dj
            if not (0 <= ni < len(input) and 0 <= nj < len(input[ni]) and input[ni][nj] == char):
                full_word = False
        count += full_word
    return count


def main():
    input = parse_input()
    res = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            res += check_word(input, i, j)
    print(res)

# python 01.py < input > output
if __name__ == '__main__':
    main()