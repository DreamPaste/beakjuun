#수 정렬하기 3

#메모리 최적화 필요

#10000까지의 숫자 저장 후 누적값만큼 출력
# 1~10000까지의 수를 모두 인덱싱하려면 10001 자리의 리스트가 필요
import sys

data=[0 for i in range(10001)]

for i in range(int(sys.stdin.readline())):
    data[int(sys.stdin.readline())]+=1
    

for i in range(10001) :
    if i!=0 :
        for c in range(data[i]):
            print(i)