import heapq
from sys import stdin

input= stdin.readline
INF = float('inf')
N, M = map(int, input().split())
graph = []
dist = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellman(start):
    dist[start] = 0
    for i in range(N):
        # 매 반복마다 모든 간선 확인
        for a, b, c in graph:
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짦은 경우
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                # 음수 순환인 경우
                if i == N - 1:
                    return True
    
    return False


#음수 순환 루프인 경우
if bellman(1):
    print(-1)

else :
    
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else  :
            print(dist[i])