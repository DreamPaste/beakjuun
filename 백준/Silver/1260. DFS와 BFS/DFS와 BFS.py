from sys import stdin as s
from collections import deque
input = s.readline

N, M, V = map(int, input().split())

# 간선 정보를 저장할 그래프
graph = {i:[] for i in range(1, N+1)}

for _ in range(M) :
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for adj in graph.values():
    adj.sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

result1 = []
result2 = []


def dfs(start):

    visited_dfs[start] = True
    result1.append(start)

    for node in graph[start]:
        if not visited_dfs[node]:
            dfs(node)


def bfs(start):

    visited_bfs[start] = True
    result2.append(start)
    que = deque([start])

    while(que):
        v = que.popleft()

        for node in graph[v]:
            if not visited_bfs[node]:
                visited_bfs[node] = True
                que.append(node)
                result2.append(node)


dfs(V)
bfs(V)

print(" ".join(map(str, result1)))
print(" ".join(map(str, result2)))