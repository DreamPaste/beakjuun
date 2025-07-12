import sys
from collections import deque, defaultdict

input = sys.stdin.readline  # 빠른 입력

N, M = map(int, input().split())
graph = defaultdict(list)

# 간선 저장 (무방향)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
components = 0
q = deque()

for node in range(1, N + 1):
    if not visited[node]:
        components += 1           # 새 컴포넌트 발견
        visited[node] = True
        q.append(node)

        # BFS
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

print(components)
