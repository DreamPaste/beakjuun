from collections import deque

def bfs(n, k):
    MAX = 100000
    visited = [-1] * (MAX + 1)  # 방문 여부 + 최단 시간 저장
    queue = deque()
    
    # 시작점
    queue.append(n)
    visited[n] = 0
    
    while queue:
        x = queue.popleft()
        
        # 목표 위치 도착 시 즉시 반환
        if x == k:
            return visited[x]
        
        # 이동 가능한 경우
        for next_x in (x * 2, x - 1, x + 1):
            if 0 <= next_x <= MAX and visited[next_x] == -1:
                # 순간이동(0초)인 경우 먼저 탐색
                if next_x == x * 2:
                    queue.appendleft(next_x)
                    visited[next_x] = visited[x]
                else:  # 걷기(1초)인 경우 뒤에 추가
                    queue.append(next_x)
                    visited[next_x] = visited[x] + 1

# 입력 받기
N, K = map(int, input().split())
print(bfs(N, K))
