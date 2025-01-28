# 미리 dp 테이블을 초기화합니다.
# dp[i]는 i를 1, 2, 3의 합으로 나타내는 경우의 수입니다.
dp = [0] * 11  # n의 최대값이 10이므로 11 크기로 설정
dp[0] = 1  # 합이 0인 경우는 아무것도 더하지 않는 1가지 경우

# dp 테이블을 채움
for i in range(1, 11):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]


T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
