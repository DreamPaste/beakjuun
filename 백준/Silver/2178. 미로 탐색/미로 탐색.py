import sys
from collections import deque

input = sys.stdin.readline

data = []

N, M = map(int, input().split())
for _ in range(N):
    data.append(list(map(int, input().strip())))

def bfs(x, y):
    visited = set()
    visited.add((x, y))
    que = deque([(x,y)])

    while que:
        (cx, cy) = que.popleft()
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx = dx + cx
            ny = dy + cy

            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited and data[nx][ny] != 0:
                    visited.add((nx, ny))
                    que.append((nx, ny))
                    data[nx][ny] = data[cx][cy] + 1

        
bfs(0,0)
print(data[N-1][M-1])