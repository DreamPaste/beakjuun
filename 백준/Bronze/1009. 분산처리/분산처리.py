import sys

# 각 숫자의 일의 자리 패턴을 미리 저장
patterns = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    last_digit = a % 10
    pattern = patterns[last_digit]
    index = (b - 1) % len(pattern)
    print(pattern[index])
