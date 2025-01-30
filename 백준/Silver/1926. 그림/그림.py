from collections import deque

# BFS 함수 정의
def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    area = 1

    # 상하좌우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        curx, cury = que.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            # 격자 범위 내이고, 아직 방문하지 않았으며, 값이 1인 경우
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and data[nx][ny] == 1:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    area += 1

    return area

# 입력 받기
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 방문 여부를 저장할 2차원 리스트 초기화
visited = [[False for _ in range(m)] for _ in range(n)]

count = 0       # 그림의 개수
max_area = 0    # 가장 큰 그림의 넓이

# 격자의 모든 셀을 순회
for i in range(n):
    for j in range(m):
        # 셀이 1이고 아직 방문하지 않았다면 새로운 그림 발견
        if data[i][j] == 1 and not visited[i][j]:
            current_area = bfs(i, j)  # BFS를 통해 그림의 넓이 계산
            count += 1                # 그림의 개수 증가
            if current_area > max_area:
                max_area = current_area  # 가장 큰 그림의 넓이 업데이트

# 결과 출력
print(count)
print(max_area)
