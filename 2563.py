#색종이 silver v

#변수
paper= [[0 for cor in range(101)] for row in range(101)]
ans=0
#입력
for t in range(int(input())) :
    
    w,h = map(int,input().split())      #여백을 입력받음
    for i in range(10):
        for j in range(10):
            
            paper[w+i][h+j]=1
            
for i in range(100) :
    ans+=sum(paper[i])
   
    
print(ans)