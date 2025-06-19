import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    ans = n // c
    if n % c:
        ans += 1
    print(ans)
