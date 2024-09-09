n = int(input())
data = list(map(int, input().split()))

dp= [1] * n

# 각 수마다 존재하는 부분 수열을 찾음
for i in range(1,n):
    for j in range(i):
        if data[i] > data[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))