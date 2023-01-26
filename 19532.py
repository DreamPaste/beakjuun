#수학은 비대면강의
#브루트포스 알고리즘: 무식하게 모든 경우를 찾음
#입력범위가 한정적이므로 반복을 통해 찾기 가능
#가감법 활용도 가능
a,b,c,d,e,f =map(int,input().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x+b*y==c and d*x+e*y==f :
            print(x,y)
