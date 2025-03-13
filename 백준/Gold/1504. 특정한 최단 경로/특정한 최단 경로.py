import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int ,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def daijkstra(start, end):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    que = []
    heapq.heappush(que,(0, start))

    while que :
        cw, cn = heapq.heappop(que)
        if dist[cn] < cw :
            continue

        for node, weight in graph[cn]: 
            
            # 다음 노드를 방문했을때의 누적 비용
            cost  = cw + weight
            # dist에 저장된 비용보다 노드를 방문했을때 누적 비용이 더 작다면 업데이트
            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(que, (cost, node))
            
        

    return dist[end]

path_v1 = daijkstra(1, v1) + daijkstra(v1, v2) + daijkstra(v2, N)
path_v2 = daijkstra(1, v2) + daijkstra(v2, v1) + daijkstra(v1, N)

minPath = min(path_v1, path_v2)

if minPath == float('inf'):
    print(-1)
else :
    print(minPath)