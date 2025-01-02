def search(K, N):
    start, end = 1, N * N  # 가능한 범위

    while start <= end:
        mid = (start + end) // 2

        # mid 이하의 값 개수 계산
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(mid // i, N)

        # 이분 탐색 조건
        if cnt >= K:
            end = mid - 1
        else:
            start = mid + 1

    return start

N = int(input())
K = int(input())
print(search(K, N))