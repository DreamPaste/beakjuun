

def run(N, M, data):
    cnt = 0 #i,j쌍의 개수
    remain = [0] * M # 나머지를 보관하는 배열
    prefix_sum = 0 # 현재의 누적값 업데이트

    remain[0] = 1 #누적합이 0인 경우를 처리하기 위해 초기값 설정
    for i in range(N):
        #누적합 만들기
        prefix_sum += data[i]

        remainder = prefix_sum % M
        # 음수일 경우 양수로 변환해줘야 함
        if remainder < 0 : 
            remainder += M
        #나머지를 배열에 저장
        remain[remainder] +=1

    #print(remain)
    for i in remain :
        #같은 나머지를 가진 누적합 중에서 두 개를 고르는 경우
        cnt+= i*(i-1)//2


    
        


    return cnt



N, M = map(int, input().split())
data = list(map(int, input().split()))
print(run(N, M, data))