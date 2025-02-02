import sys, collections

input = sys.stdin.readline

N, M, R = map(int, input().split())

# 인접 리스트 생성: 0번 인덱스는 사용하지 않음
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = [0] * (N+1)
cnt = 1

# 간선 정보 입력 및 양방향 그래프 구성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 내림차순 방문을 위해 각 정점의 인접 리스트를 내림차순 정렬
for i in range(1, N+1):
    graph[i].sort(reverse=True)

def bfs(r):
    global cnt
    que = collections.deque([r])
    visited[r] = True
    result[r] = cnt
    cnt += 1

    while que:
        node = que.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                que.append(next_node)
                result[next_node] = cnt
                cnt += 1

bfs(R)

for i in range(1, N+1):
    print(result[i])
