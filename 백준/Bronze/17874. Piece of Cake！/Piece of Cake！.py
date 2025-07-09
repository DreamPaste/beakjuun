# 입력: n(케이크 한 변 길이), h(위쪽에서 가로 컷 위치), v(왼쪽에서 세로 컷 위치)
n, h, v = map(int, input().split())

# 가로 길이 중 큰 값, 세로 길이 중 큰 값 계산
max_height = max(h, n - h)
max_width  = max(v, n - v)

# 부피 계산 (두께 4cm)
volume = max_height * max_width * 4

# 결과 출력
print(volume)
