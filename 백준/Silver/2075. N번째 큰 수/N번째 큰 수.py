import sys
import heapq

input = sys.stdin.readline     # [변경] main 안이 아니라 스크립트 최상단에서 바로 설정

N = int(input())              # 배열의 크기 N
min_heap = []                 # 최소 힙으로 사용할 리스트

for _ in range(N):
    for num in map(int, input().split()):
        heapq.heappush(min_heap, num)
        if len(min_heap) > N:
            heapq.heappop(min_heap)

# 힙의 루트가 N번째로 큰 수
print(min_heap[0])            # [변경] main 함수 호출 없이 바로 출력
