import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    files= list(map(int, input().split()))
    
    dp=[[0] * k for _ in range(k)]
    prefix = [files[0]] * k
    #0부터 더할때 -1인덱스를 0으로 만들기 위함
    prefix.append(0)
    # i 부터 j 까지 합치는데 필요한 최소 비용
    for i in range(1, k):
        for j in range(k-i):
            
            #dp[0][1], dp[1][2], dp[2][3]... 일때는 이어진 두 페이지의 합을 먼저 구함
            #prefix 배열에 누적합을 저장
            if i == 1 :
                dp[j][i+j] = files[j] + files[j+1]
                prefix[i+j] = prefix[j] + files[i+j]
            
            # dp[j][i+j] = sum(j:i+j) + min(dp[0][2](ABC) + dp[3][3](D), dp[1][2](AB) + dp[2][3](CD), dp[0][0](A) + dp[1,3](BCD))
                                      # min(for mid in range(j,i+j):  dp[j][mid] + dp[mid][i+j])
            else :
                #sum(j : i+j)
                sumdata=  prefix[i+j] - prefix[j-1]
                #print(f"dp[{j}][{j+i}] = sumdata({sumdata} + min({j}~{i+j}))")
                #print("최소값 탐색중..")
                mincost = math.inf
                for mid in range(j, i+j):
                    #print(f"dp[{j}][{mid}]({dp[j][mid]}) + dp[{mid+1}][{i+j}]({dp[mid+1][i+j]}) = {dp[j][mid] + dp[mid+1][i+j]}")
                    mincost = min(mincost, dp[j][mid] + dp[mid+1][i+j])
                dp[j][i+j] = sumdata + mincost
                # print("최적값 계산 완료")
                # print(f"sum({sumdata}) + min({mincost}) = {dp[j][i+j]}")
                # print()
                # for line in dp:
                #     for el in line:
                #         print("%04d" %el, end=" ")
                #     print()

                
            #dp[j][j+i] = sum(files[j:i+j]) 
    print(dp[0][k-1])
