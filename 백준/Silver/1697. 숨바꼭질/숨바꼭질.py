import sys
from collections import deque

def bfs(start, target):
  
    MAX = 100001 
    visited = [-1] * MAX  # 방문 여부 및 이동 횟수를 기록 (-1은 미방문)
    queue = deque()
    
    # 시작 위치 설정
    visited[start] = 0  
    queue.append(start)
    
    # BFS 탐색
    while queue:
        current = queue.popleft()
        
        # 목표 위치에 도달하면 현재까지 걸린 시간(이동 횟수)를 반환
        if current == target:
            return visited[current]
        
        # 현재 위치에서 이동 가능한 3가지 경우
        for next_pos in (current - 1, current + 1, current * 2):
            # 범위 내이고 아직 방문하지 않은 위치인 경우
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1  # 이동 횟수 갱신
                queue.append(next_pos)
                
N, K = map(int, sys.stdin.readline().strip().split())
result = bfs(N, K)
sys.stdout.write(str(result))
