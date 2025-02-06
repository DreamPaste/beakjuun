import sys

input = sys.stdin.readline

N = int(input())
data=[]
for _ in range(N):
    r, c = map(int, input().split())
    data.append((r, c))

dp = [[0]*N for _ in range(N)]

for l in range(1,N):
    for i in range(N-l):
        j = l+i
        dp[i][j] = float('inf')
        for mid in range(i, j):
            #dp[i][mid] + dp[mid+1][j] : A*BCD, AB*CD, A*BCD .. 형태의 비용
            cost = dp[i][mid] + dp[mid+1][j]
            # 왼쪽 행렬의 행 * 공통 차원 * 오른쪽 행렬의 열
            cost += data[i][0] * data[mid][1] * data[j][1]
            dp[i][j] = min(dp[i][j], cost)
        
print(dp[0][N-1])

"""
dp[i][j] : i부터 j까지 곱할때 최소 곱셈 연산 횟수
    A       B       C       D

A   0       AB      AB*C    A*BCD
                    A*BC    AB*CD
                            ABC*D

B           0       BC      BC*D
                            B*CD

C                   0       CD

D                           0
"""