from sys import stdin
from collections import deque
input = stdin.readline


M, N = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

def bfs():

    que = deque()
    visited = set()
    #벽 개수 세기 
    wallCount =0
    #큐에 익은 토마토 모두 넣기
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                que.append((i,j))
                visited.add((i,j))
            elif data[i][j] == -1:
                wallCount +=1
    #저장될 때부터 모든 토마토가 익었다면 0 출력
    if wallCount + len(visited) == N * M:
        return 0
    maxDay = 0
    while que:
        cx, cy = que.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            
            nx = dx + cx
            ny = dy + cy

            if 0<= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited and data[nx][ny] == 0 :
                    que.append((nx, ny))
                    visited.add((nx, ny))
                    
                    data[nx][ny] = data[cx][cy] + 1
                    maxDay = max(maxDay, data[nx][ny])
    
    return maxDay -1

result = bfs()    
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            result = -1
            break

print(result)



