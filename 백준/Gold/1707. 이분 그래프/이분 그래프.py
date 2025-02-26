import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V + 1)
    isBipartite = True

    for i in range(1, V + 1):
        if visited[i] == 0:
            que = deque([i])
            visited[i] = 1 

            while que and isBipartite:
                cur = que.popleft()
                for neighbor in graph[cur]: 
                    if visited[neighbor] == 0:
                        visited[neighbor] = -visited[cur]
                        que.append(neighbor)
                    elif visited[neighbor] == visited[cur]:
                        isBipartite = False
                        break
        if not isBipartite:
            break

    print("YES" if isBipartite else "NO")
