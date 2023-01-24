#베르트랑 공준
#소수 찾기(에라토스테네스의 체)+미리 소수 판별

# 소수 판별
def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True	

#소수 데이터
m=123456
data=[]
for i in range(2,m*2+1):
    if sosu(i):
        data.append(i)



while True:
    n = int(input())

    if n==0:    
        break

    cnt=0

    for i in data :
        if n< i <= 2*n :
            cnt+=1

    print(cnt)