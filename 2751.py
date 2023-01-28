#수 정렬하기
import sys

input  = sys.stdin.readline

data=[]
N = int(input())
for l in range(N):
    data.append(int(input()))

data = sorted(data)

for i in data:
    print(i)