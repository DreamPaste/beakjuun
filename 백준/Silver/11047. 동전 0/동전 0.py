
N, K = map(int, input().split())
coins = list( int(input()) for _ in range(N))
coins.sort(reverse=True)
min_cnt = 0
for coin in coins:
    if K == 0:
        break
    if coin <= K:
        min_cnt += K // coin  # 해당 동전으로 필요한 개수 계산
        K %= coin    
    

print(min_cnt)