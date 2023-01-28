#통계학

#배열의 중앙을 중심으로 음수와 양수를 나눈다.
import sys
input = sys.stdin.readline

data = [0 for i in range(8002)]
n = int(input())
for case in range(n) :
    num = int(input())
    data[num+4000]+=1  
    

#산술평균
sums=0
cnt=0
mode_cnt=0
mode_trigger =False             # 최빈값
low_trigger = False             # 최소값
high=0             # 최대값
for i in range(8002) :
    if data[i]!=0:
        if cnt< n//2+1 <=cnt+data[i] :  #중앙값 저장
             half = i-4000

        cnt+=data[i]
        if mode_cnt <= data[i] :       #두번째로 작은 최빈값이 나오면 최빈값 검사 안함
           
            if mode_cnt == data[i] and mode_trigger == False : 
                mode_trigger = True
                mode = i - 4000

            elif mode_cnt < data[i] :
                mode_cnt = data[i]
                mode_trigger = False
                mode = i - 4000
            
        if low_trigger == False : #최소값
            low_trigger = True
            low = i -4000
        
        high = i-4000 #최대값 (값이 마지막으로 바뀐 이후 모두 data[i] 가 0이라면 안바뀜)
        
        sums+=(i-4000)*data[i]
        #print("%d가 %d개 있습니다"%(i-4000,data[i]))

if sums >= 0 : #round 함수는 오사오입이므로 사용 x
    aver = int(sums/n + 0.5)
else :
    aver = int(sums/n - 0.5)

print(aver)
print(half)
print(mode)
print(high-low)
