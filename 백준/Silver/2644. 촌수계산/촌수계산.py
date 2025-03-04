import sys

input = sys.stdin.readline

n = int(input())
tx, ty = map(int, input().split())
if tx > ty : (tx, ty) = (ty, tx)
graph = {i:[] for i in range(1,n+1)}
visited =set()
m = int(input())

for _ in range(m):
    #x는 y의 부모 번호임
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, target, cnt):
    visited.add(start)
    if start == target:
        return cnt
    for next_node in graph[start]:
        if next_node not in visited:
            result = dfs(next_node, target, cnt+1)
            if result != -1:
                return result
    return -1



print(dfs(tx, ty, 0))