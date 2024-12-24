from sys import stdin
input = stdin.readline




def param_binary_search(start, end) :
    #print("func()", start, end)
    if start > end : 
        return end

    n = 0
    mid = (start + end) // 2
    for lan in arr_LAN :
       #랜선을 mid 개수로 자름
       n += lan // mid 
    #print(n , mid)
    #N개 이상으로 잘랐다면 더 긴 랜선의 길이 탐색
    if n >= N :
        return param_binary_search(mid + 1, end)
    #N개보다 작게 잘랐다면 더 작은 길이 탐색
    else :
        return param_binary_search(start, mid - 1)
    
    
K, N = map(int, input().split())
arr_LAN =[int(input().strip()) for _ in range(K)]

print(param_binary_search(1, max(arr_LAN)))
