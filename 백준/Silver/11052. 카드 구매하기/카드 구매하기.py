
N = int(input())
cardpacks =list(map(int, input().split()))

#i개를 구매하는데 필요한 최대 비용
dp = [0] * (N+1)
#1 5 6 7
# dp[0] : 0개를 구매하는 비용 0
# dp[1] : 1개를 구매하는 비용 1
# dp[2] : 2개를 구매하는 비용
    # 2개짜리 카드팩을 삼 : 5
    # 이전 최댓값인 dp[1] + 1개 카드팩 구매 1 : 1+1 = 2

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + cardpacks[j-1])

print(dp[N])