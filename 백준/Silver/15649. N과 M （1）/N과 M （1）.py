N, M = map(int, input().split())

res = []
visited=[False for _ in range(N+1)]

def dfs():
    if len(res) == M:
        print(' '.join(map(str,res)))

        return

    for i in range(1, N+1):
        #방문한경우 제외
        if visited[i]:
            continue
        #방문하지 않은경우
        visited[i] = True
        res.append(i)
        dfs()
        #이전 상황으로 back
        res.pop()
        visited[i]=False

dfs()