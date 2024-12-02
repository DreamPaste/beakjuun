N = int(input())

A = list(map(int, input().split()))

M = int(input())

mlist = list(map(int, input().split()))

A.sort()
# 이진 탐색 함수 정의
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스 계산
        if arr[mid] == target:  # 값을 찾았을 때
            return 1
        elif arr[mid] < target:  # 타겟 값이 더 클 경우
            start = mid + 1
        else:  # 타겟 값이 더 작을 경우
            end = mid - 1
    return 0  # 값을 찾지 못했을 때

# mlist의 각 값에 대해 A에서 탐색
for i in mlist:
    print(binary_search(A, i))