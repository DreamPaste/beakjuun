import sys

input = sys.stdin.readline


W = int(input())
weights = list(map(int, input().split()))
B = int(input())
balls = list(map(int, input().split()))
# 모든 추를 사용할때 최대 무게
total = sum(weights)
# 만들수 있는 무게
dp = [False] * (total + 1) 
dp[0] = True # 아무 추도 사용하지 않은 경우

for weight in weights:
    newDP =dp[:]

    for d in range(total+1):
        if dp[d]:
            #추를 왼쪽 올려서 차이가 d + weight이 되는 경우
            if d + weight <= total:
                newDP[d + weight] = True
            #추를 오른쪽에 올려서 차이가 d - weight이 되는 경우
            newDP[abs(d - weight)] = True

    dp  = newDP

res = []

for ball in balls:
    if ball > total:
        res.append("N")
    elif dp[ball]:
        res.append("Y")
    else : 
        res.append("N")

print(" ".join(res))