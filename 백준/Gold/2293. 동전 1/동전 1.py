import sys
input = sys.stdin.readline


N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))


dp = [0] * (K + 1)
dp[0] = 1

for coin in coins:
    
    for x in range(coin, K + 1):
        dp[x] += dp[x - coin]

print(dp[K])
