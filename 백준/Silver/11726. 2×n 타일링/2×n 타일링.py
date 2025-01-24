n = int(input())
dp = [0] * (n+1)
#indexERR 방지
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 2
if n > 2:
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])

# 1 == 1
# |
# 2 == 2
# =, ||
# 3 == 2 + 1
# =|, |=, |||
# 4 == 5
# ==, ||| |, =| |, |= |, ||=
# 5
# ==|, |||||, =|||, |=||, ||=|, =|=, |==, |||=
# n-2 개의 모양에 =을 이어붙인 값 + n-1개의 모양에 |을 어어붙인값
