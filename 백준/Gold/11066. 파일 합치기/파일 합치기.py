import sys

def file_merge_min_cost(k, files):
    # 누적 합 계산
    prefix_sum = [0] * (k + 1)
    for i in range(k):
        prefix_sum[i + 1] = prefix_sum[i] + files[i]
    
    # DP 테이블 및 최적 분할 지점 테이블 초기화
    dp = [[0] * k for _ in range(k)]
    opt = [[0] * k for _ in range(k)]
    
    for i in range(k):
        opt[i][i] = i  # 초기 조건: 같은 파일은 비용 0
    
    # 구간의 길이별로 최소 비용 계산
    for length in range(1, k):
        for i in range(k - length):
            j = i + length
            dp[i][j] = float('inf')
            
            # Knuth 최적화를 위한 k 탐색 범위 설정
            start = opt[i][j - 1]
            end = opt[i + 1][j] if (i + 1) < k else j - 1
            if end < start:
                end = start  # 범위를 벗어나지 않도록 조정
            
            # 최적의 k를 찾아 최소 비용 계산
            for m in range(start, end + 1):
                if m >= j:
                    continue  # 유효한 범위 내에서만 계산
                cost = dp[i][m] + dp[m + 1][j] + prefix_sum[j + 1] - prefix_sum[i]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    opt[i][j] = m  # 최적의 k 저장
    
    return dp[0][k - 1]

# 입력 전체를 한 번에 읽어 처리
data = sys.stdin.read().split()
idx = 0
T = int(data[idx]); idx += 1

for _ in range(T):
    k = int(data[idx]); idx += 1
    files = list(map(int, data[idx:idx + k])); idx += k
    result = file_merge_min_cost(k, files)
    print(result)
