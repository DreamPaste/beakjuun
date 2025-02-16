import sys,math

input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

total_costs = sum(costs)
# 각 비용을 지불하는 경우의 최대 메모리
dp = [0]* (total_costs+1) 
dp[0] = 0

for app in range(n):
    #앱마다 역순으로 업데이트하며 앱 중복 방지 및 costs[app]이 cost보다 큰 경우 방지
    for cost in range(total_costs, costs[app] -1, -1):
        
        #앱을 제거하고 비용을 지불하여 메모리를 확보하는 경우
        app_exit_memory = dp[cost - costs[app]] + memories[app]
        
        dp[cost] = max(dp[cost], app_exit_memory)

for cost in range(total_costs+1):
    #확보한 메모리가 m바이트 이상인 경우
    if dp[cost] >= m:
        print(cost)
        break
            

