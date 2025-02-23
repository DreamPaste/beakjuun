import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
# 입력 데이터를 2차원 리스트(grid)로 저장
grid = [list(map(int, list(input().strip()))) for _ in range(N)]

# visited[x][y][0]: (x, y)에 도달했을 때 벽을 부수지 않은 경우 방문 여부
# visited[x][y][1]: (x, y)에 도달했을 때 벽을 부순 경우 방문 여부
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

def bfs():
    # 큐에는 (x, y, 벽부순여부, 현재까지 거리)를 저장합니다.
    dq = collections.deque()
    dq.append((0, 0, 0, 1))
    visited[0][0][0] = True  # 시작점 방문 처리 (벽 부수지 않은 상태)
    
    while dq:
        x, y, broken, dist = dq.popleft()
        
        # 목표 지점에 도달하면 현재까지의 거리를 반환
        if x == N - 1 and y == M - 1:
            return dist
        
        # 네 방향으로 이동
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 이동할 칸이 0(길)이고, 해당 상태에서 방문하지 않은 경우
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    dq.append((nx, ny, broken, dist + 1))
                # 이동할 칸이 1(벽)이고 아직 벽을 부수지 않았다면
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    dq.append((nx, ny, 1, dist + 1))
    return -1

print(bfs())
