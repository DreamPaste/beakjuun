import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정 (트리 깊이가 클 수 있어서)

# 입력 받기
N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]  # 인접 리스트
parent = [0] * (N + 1)  # 부모 저장 배열

# 트리 연결 정보 입력
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS로 부모 찾기
def dfs(node):
    for next_node in graph[node]:
        if parent[next_node] == 0:  # 방문 안 했으면
            parent[next_node] = node  # 현재 노드를 부모로 저장
            dfs(next_node)  # 다음 노드로 재귀 탐색

parent[1] = -1  # 루트 노드의 부모를 특별히 -1로 설정
dfs(1)  # 1번 노드부터 시작

# 결과 출력 (2번 노드부터)
for i in range(2, N + 1):
    print(parent[i])
