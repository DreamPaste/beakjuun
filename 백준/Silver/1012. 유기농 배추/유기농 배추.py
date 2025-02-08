import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y, M, N, grid):
    # 범위를 벗어나거나 배추가 없는 경우 
    if x < 0 or x >= M or y < 0 or y >= N or grid[y][x] == 0:
        return
   
    grid[y][x] = 0
    # 상하좌우로 DFS 진행
    dfs(x+1, y, M, N, grid)
    dfs(x-1, y, M, N, grid)
    dfs(x, y+1, M, N, grid)
    dfs(x, y-1, M, N, grid)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1  # 배추가 심어진 위치는 1로 표시
    
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                dfs(j, i, M, N, grid)
                count += 1 
    print(count)
