from collections import deque

T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    priority_list = list(map(int, input().split())) 
    print_que = deque([(priority_list[i], i) for i in range(N)])
    # 출력할 내용이 한 개 뿐이라면 즉시 출력
    if N == 1 :
        print(1)
        continue

    cnt =0
    
    while print_que :
        #1 현재 queue의 가장 앞에 있는 문서의 중요도를 확인한다.
        current = print_que.popleft()
        

        #2 나머지 문서들 중 더 중요도가 높다면 큐의 뒤로 보냄
        
        if any(current[0] < item[0] for item in print_que) :
            print_que.append(current)

        else :
            cnt+=1
            
            if current[1] == M :
                print(cnt)
                break
            


            
    