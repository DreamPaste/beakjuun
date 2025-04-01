import sys
input = sys.stdin.readline

# 입력 받기: 용액의 개수와 각 용액의 특성값 리스트
n = int(input())
arr = list(map(int, input().split()))

# 1. 리스트 정렬
arr.sort()  # 오름차순 정렬

# 2. 두 포인터 초기화 및 변수 설정
left, right = 0, n - 1
best_sum = float('inf')  # 현재까지 발견된 합의 절대값의 최솟값 (초기에는 무한대로 설정)
best_pair = (0, 0)       # 최적의 두 용액 저장

    # 3. 두 포인터를 이용한 최적의 두 용액 탐색
while left < right:
        current_sum = arr[left] + arr[right]

        # 현재 합의 절대값이 최적값보다 작으면 갱신
        if abs(current_sum) < best_sum:
            best_sum = abs(current_sum)
            best_pair = (arr[left], arr[right])
        
        # 합이 음수이면 왼쪽 포인터 이동 (더 큰 수로)
        if current_sum < 0:
            left += 1
        # 합이 양수이면 오른쪽 포인터 이동 (더 작은 수로)
        elif current_sum > 0:
            right -= 1
        else:
            # 합이 0이면 최적해이므로 바로 종료
            best_pair = (arr[left], arr[right])
            break

    # 4. 결과 출력
print(best_pair[0], best_pair[1])
