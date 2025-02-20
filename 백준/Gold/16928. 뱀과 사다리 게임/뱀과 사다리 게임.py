import sys
from collections import deque
input = sys.stdin.readline

graph = [0] * 101
potal = [i for i in range(101)]
N, M = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())
    potal[x] = y

for _ in range(M):
    u, v = map(int, input().split()) 
    potal[u] = v

def bfs():

    que = deque([1])
    visited = set([1])

    while que:
        cur = que.popleft()
        
        if cur == 100 :
            return graph[cur]
        #주사위 굴림
        for i in range(1,7):
            next = cur + i

            if next <= 100:
                next = potal[next]
                if next not in visited:
                    que.append(next)
                    visited.add(next)
                    graph[next] = graph[cur] + 1
    return -1
print(bfs())
