#통계학

#배열의 중앙을 중심으로 음수와 양수를 나눈다.
import sys
input = sys.stdin.readline

data = [0 for i in range(8001)]
for n in range(int(input())) :
    num = int(input())
    if num>=0 :
        data[num+4000]+=1
    else :
        data[abs(num)]+=1