import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = {i : [] for i in range(1,N+1)}
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited[start] = True

    for next in graph[start]:
        if not visited[next]:
            dfs(next)

dfs(1)
# 0번 인덱스는 필요없음
print(sum(visited) - 1)