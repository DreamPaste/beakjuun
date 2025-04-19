import sys
import heapq

# 읽어들인 모든 토큰을 한 번에 분리
data = sys.stdin.read().split()
it = iter(data)

# 테스트 케이스 수
T = int(next(it))

for _ in range(T):
    # M개의 숫자 입력
    M = int(next(it))
    left = []   # 최대 힙 (부호 반전 저장)
    right = []  # 최소 힙
    medians = []

    # 스트림 처리
    for i in range(M):
        num = int(next(it))

        # 1) 삽입 위치 결정
        if not left or num <= -left[0]:
            heapq.heappush(left, -num)     # 최대 힙처럼
        else:
            heapq.heappush(right, num)     # 최소 힙

        # 2) 힙 균형 맞추기
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(left) < len(right):
            heapq.heappush(left, -heapq.heappop(right))

        # 3) 홀수 번째 입력일 때 중앙값 기록 (i가 0부터 시작하므로 i%2==0)
        if i % 2 == 0:
            medians.append(-left[0])

    # 4) 결과 출력
    print(len(medians))
    for idx, m in enumerate(medians):
        end_char = '\n' if (idx + 1) % 10 == 0 or idx == len(medians) - 1 else ' '
        print(m, end=end_char)
