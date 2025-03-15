from sys import stdin
import heapq
input = stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, start))  # (현재까지 거리, 특수 간선 사용 여부, 정점)
    distance[start] = 0
    flag[start] = 0
    while q:
        cur_dist, cur_used, cur_node = heapq.heappop(q)
        # 이미 더 좋은 상태가 저장되어 있다면 건너뜁니다.
        if cur_dist > distance[cur_node] or (cur_dist == distance[cur_node] and cur_used > flag[cur_node]):
            continue
        for next_node, next_weight in graph[cur_node]:
            new_cost = cur_dist + next_weight
            # 현재 간선이 (g, h) 또는 (h, g)인지 확인
            if (cur_node, next_node) == (g, h) or (cur_node, next_node) == (h, g):
                new_used = -1
            else:
                new_used = cur_used
            # 새 상태가 더 좋으면 업데이트합니다.
            if new_cost < distance[next_node] or (new_cost == distance[next_node] and new_used < flag[next_node]):
                distance[next_node] = new_cost
                flag[next_node] = new_used
                heapq.heappush(q, (new_cost, new_used, next_node))

T = int(input())
ans = []

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    # 각 정점의 최단 거리와 특수 간선 사용 여부를 관리합니다.
    distance = [INF] * (n + 1)
    flag = [INF] * (n + 1)  # -1: 특수 간선 사용, 0: 사용하지 않음 (초기값은 INF로 설정)
    dests = set()

    for _ in range(m):
       a, b, d = map(int, input().split())
       graph[a].append((b, d))
       graph[b].append((a, d))

    for _ in range(t):
       dests.add(int(input()))

    dijkstra(s)

    # flag가 -1인 정점: (g, h) 간선을 사용한 최단 경로
    trueflag = {x for x in range(1, n+1) if flag[x] == -1}
    resList = sorted(dests.intersection(trueflag))
    ans.append(resList)

for answer in ans:
    print(" ".join(map(str, answer)))
