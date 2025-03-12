import sys

input= sys.stdin.readline

N = int(input())
data=[(0, 0)]
for _ in range(N):
  t, p = map(int, input().split())
  data.append((t, p))


dp =[0] * (N + 2)
# N = 7
#days: 1  2  3  4  5  6  7
#i=1 : 10 10 10 
#i=2 : 10 20 20 20 20
#i=3 : 10 20 20 20 20
#i=4 : 10 20 20 
for i in range(N, 0, -1):

  # 상담일이 퇴사일을 넘기면 상담 불가능
  if i + data[i][0] > N + 1:
    dp[i] = dp[i+1]

  else :
    dp[i] = max(dp[i+1], data[i][1] + dp[i + data[i][0]]) 
print(dp[1])
    

