import sys

def parse_input():
    return [line.strip('\r\n') for line in sys.stdin]

def check_word(input: list[str], i: int, j: int):
    word = "MAS"
    if input[i][j] != word[1]:
        return 0
    dirs = [(1, 1), (-1, 1)]
    cross = True
    for di, dj in dirs:
        ni1, nj1 = i + di, j + dj
        ni2, nj2 = i - di, j - dj
        if not (0 <= ni1 < len(input) and 0 <= nj1 < len(input[ni1])):
            cross = False
            break
        if not (0 <= ni2 < len(input) and 0 <= nj2 < len(input[ni2])):
            cross = False
            break
        if not (input[ni1][nj1] == word[2] and input[ni2][nj2] == word[0] or input[ni1][nj1] == word[0] and input[ni2][nj2] == word[2]):
            cross = False
            break
    return cross


def main():
    input = parse_input()
    res = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            res += check_word(input, i, j)
    print(res)

# python 02.py < input > output
if __name__ == '__main__':
    main()