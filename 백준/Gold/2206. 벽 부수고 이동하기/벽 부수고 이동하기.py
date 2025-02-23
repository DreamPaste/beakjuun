import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
# 입력 받은 문자열을 정수 리스트로 변환합니다.
grid = [list(map(int, list(input().strip()))) for _ in range(N)]

# visited[x][y][0]: (x,y)에 도달했을 때 벽을 부수지 않은 경우 방문 여부
# visited[x][y][1]: (x,y)에 도달했을 때 벽을 부순 경우 방문 여부
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

def bfs():
    # 큐에는 (x, y, 벽부순여부, 현재까지 거리)를 저장합니다.
    dq = collections.deque()
    dq.append((0, 0, 0, 1))
    visited[0][0][0] = True
    
    while dq:
        x, y, w, d = dq.popleft()
        
        # 목표 지점에 도달하면 현재 거리를 반환
        if x == N - 1 and y == M - 1:
            return d
        
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                # 이동 가능한 칸(0)이고 아직 방문하지 않은 경우
                if grid[nx][ny] == 0 and not visited[nx][ny][w]:
                    visited[nx][ny][w] = True
                    dq.append((nx, ny, w, d + 1))
                # 벽(1)이고 아직 벽 부수기를 사용하지 않은 경우
                if grid[nx][ny] == 1 and w == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    dq.append((nx, ny, 1, d + 1))
    
    return -1

print(bfs())
