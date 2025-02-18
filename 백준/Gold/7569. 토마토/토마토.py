from sys import stdin
from collections import deque
input = stdin.readline

# M 가로
# N 세로
# H 높이
M, N, H = map(int, input().split())
data = [[]for _ in range(H)]
for h in range(H):
    for _ in range(N):
        data[h].append(list(map(int, input().split())))

def bfs():

    que = deque()
    visited = set()
    #빈 토마토 개수
    emptyCount =0
    #큐에 익은 토마토 모두 넣기
    #x: 가로, y: 세로, z: 높이
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if data[z][y][x] == 1:
                    que.append((x, y, z))
                    visited.add((x, y, z))
                elif data[z][y][x] == -1:
                    emptyCount +=1

    #저장될 때부터 모든 토마토가 익었다면 0 출력(빈곳 + 익은곳)
    if emptyCount + len(visited) == H * N * M:
        return 0
    
    maxDay = 0
    while que:
        
        cx, cy, cz = que.popleft()
        for dx, dy, dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            
            nx = dx + cx
            ny = dy + cy
            nz = dz + cz
            # 경계 설정
            if 0<= nx < M and 0 <= ny < N and 0 <= nz < H:
                if (nx, ny, nz) not in visited and data[nz][ny][nx] == 0 :
                    que.append((nx, ny, nz))
                    visited.add((nx, ny, nz))
                    #익어가는 날짜 업데이트
                    data[nz][ny][nx] = data[cz][cy][cx] + 1
                    maxDay = max(maxDay, data[nz][ny][nx])
    
    return maxDay -1

result = bfs()
for z in range(H):    
    for y in range(N):
        for x in range(M):
            if data[z][y][x] == 0:
                result = -1
                break

print(result)



