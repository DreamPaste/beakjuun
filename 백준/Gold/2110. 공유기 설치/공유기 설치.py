
# N개의 집, x1 형태의 좌표
# 집에 공유기 c개 설치
# 한 집에는 공유기를 하나만 설치할 수 있고,인접한 공유기 사이의 거리는 최대로
# 인접한 공유기의 최소 거리(1,4 => 3)를 최대로 해야함 

N, C = map(int, input().split())

homes = [int(input()) for _ in range(N)]

homes.sort()

def search(start, end):

    if start > end:
        return end
    
    mid= (start+end)//2
    device = 1
    current= homes[0]
    for i in range(1,N):
        
        # 공유기를 설치할 거리가 공유기 최소 설치 거리보다 길다면
        if homes[i] - current >= mid :
            # 공유기 설치
            current = homes[i]
            device+=1
        
    #print(mid,device)
# 공유기 설치가 C값을 초과했다면 공유기 설치 거리를 늘린다
    if device >= C : 
        return search(mid+1, end)
# 공유기 설치가 C값을 만족하지 못한다면 공유기 설치 거리를 줄인다.
    else :
        return search(start, mid-1)


print(search(1,homes[-1]))