import sys
input = sys.stdin.readline

# 입력
n, k, T = map(int, input().split())
d = list(map(int, input().split()))

# 불쾌함 지수 누적 변수
discomfort = 0

# 시뮬레이션 루프
for i in range(n):
    if T > k:
        # 너무 뜨거우면 차갑게 조절
        T = T + d[i] - abs(T - k)
    elif T < k:
        # 너무 차가우면 뜨겁게 조절
        T = T + d[i] + abs(T - k)
    else:
        # 적정 온도면 그대로
        T = T + d[i]
    discomfort += abs(T - k)

# 결과 출력
print(discomfort)
