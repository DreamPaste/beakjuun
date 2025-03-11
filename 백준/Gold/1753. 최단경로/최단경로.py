import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, V):
    distance = [INF] * (V + 1)
    queue = []

    # 시작 노드 거리 초기화
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        # 이미 처리된 노드는 무시
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for next_node, weight in graph[now]:
            cost = dist + weight
            # 더 짧은 경로 발견 시 업데이트
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return distance

# 입력
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 실행
result = dijkstra(K, graph, V)

# 출력
for i in range(1, V + 1):
    print("INF" if result[i] == INF else result[i])
