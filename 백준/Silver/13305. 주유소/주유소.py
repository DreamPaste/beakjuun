N = int(input()) # 2<=N<=100,000
roads =list(map(int, input().split())) # 도시들의 연결 길이(N-1)
olis = list(map(int, input().split())) # 도사당 리터 가격

# 특정 도시 i의 리터당 가격이 이후 방문할 도시들의 가격보다 저렴하다면,
#  도시 i의 가격보다 저렴한 도시를 방문 전까지의 기름을 모두 구매

total_cost = 0
min_oli = olis[0]
min_index =0
for i in range(1,N) :
    # i번쨰 방문한 도시가 min_oli 도시의 기름보다 저렴하다면,
    #해당 구간 거리만큼 기름을 구매
    
    #print(f"min oli[{min_index}]: ",min_oli, f"olis[{i}]: ",olis[i])
    if  min_oli >= olis[i] or i==N-1:  
        total_cost += sum(roads[min_index : i])*min_oli
        #print("total: ",sum(roads[min_index : i]),' * ',min_oli, " = ", total_cost)

        min_oli = olis[i]
        min_index = i
        
        #print(f'chage => min oli[{min_index}] :', min_oli, )    
    


print(total_cost)