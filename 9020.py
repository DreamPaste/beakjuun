#골드바흐의 추측

# 소수 판별
def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True	

#연산

for case in range(int(input())):
    n = int(input())

    for i in range(n//2,1,-1): #n의 반절부터 줄어들며 값을찾음
        if sosu(i) and sosu(n-i):    # 두 숫자가 소수에 존재할때     
            print(i,n-i)
            break
  