import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 크게 늘립니다.

N, M, R = map(int, input().split())

graph = {i: [] for i in range(N+1)}

for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 노드를 내림차순으로 정렬
for adj in graph.values():
    adj.sort(reverse=True)

result = [0] * (N + 1)
count = 1  # 방문 순서 카운트

visted = [False] * (N+1)

def dfs(r): 
    global count
    visted[r] = True
    result[r] = count
    count +=1
    
    for x in graph[r] :
        if not visted[x] :
            dfs(x)


dfs(R)

# DFS 수행 후 결과 출력
for i in range(1, N + 1):
    print(result[i])