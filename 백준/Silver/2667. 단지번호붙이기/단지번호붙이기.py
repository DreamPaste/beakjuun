import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
houseMap =[]
for _ in range(N):
    houseMap.append(list(map(int, input().strip())))

visited = [[False] * N for _ in range(N)]
result = []
def bfs(x, y):
    
    cnt = 1
    que = deque([(x,y)])
    visited[x][y] = True
    while que:
        (cx,cy) = que.popleft()
        
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if houseMap[nx][ny] == 1 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    cnt+=1
    
    return cnt

for i in range(N):
    for j in range(N):
        if houseMap[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(len(result))
result.sort()
print("\n".join(map(str, result)))

