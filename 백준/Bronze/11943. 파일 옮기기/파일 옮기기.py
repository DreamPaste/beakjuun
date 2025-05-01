# 입력: 첫 줄에 A, B / 둘째 줄에 C, D
A, B = map(int, input().split())
C, D = map(int, input().split())

# 두 가지 옵션 중 최소 이동 횟수 계산
result = min(B + C, A + D)

# 결과 출력
print(result)