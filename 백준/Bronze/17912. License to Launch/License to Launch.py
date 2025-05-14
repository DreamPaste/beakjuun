# 1. 입력 받기
n = int(input())                             # 날짜 수 n
space_junk = list(map(int, input().split()))  # 각 날의 우주 쓰레기 양 리스트

# 2. 최소값과 발사일 초기화
min_junk = space_junk[0]  # 현재까지의 최소 우주 쓰레기 양
launch_day = 0            # 최소값이 처음 등장하는 인덱스

# 3. 순회하며 최소값 갱신
for i in range(1, n):
    if space_junk[i] < min_junk:
        min_junk = space_junk[i]  # 더 작은 값을 찾으면 최소값 갱신
        launch_day = i            # 해당 인덱스로 발사일 갱신

# 4. 결과 출력
print(launch_day)
