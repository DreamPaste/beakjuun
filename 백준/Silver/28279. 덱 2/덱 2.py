import sys
from collections import deque

deq = deque()
N = int(input())

for i in range(N):
    line= list(map(int, sys.stdin.readline().strip().split()))
# input func
    if line[0]==1:
        deq.appendleft(line[1])

    elif line[0] == 2:
        deq.append(line[1])
# popval func
    elif line[0] == 3:
        if(len(deq)):
            print(deq.popleft())
        else : 
            print(-1)

    elif line[0] == 4 :
        if(len(deq)):
            print(deq.pop())
        else :
            print(-1)
# getLength func
    elif line[0] == 5:
        print(len(deq))

# isEmpty func
    elif line[0] == 6 :
        print(0 if(len(deq)) else 1)

#  getval func
    elif line[0] == 7:
        if(len(deq)):
            print(deq[0])
        else : 
            print(-1)

    elif line[0] == 8 :
        if(len(deq)):
            print(deq[-1])
        else :
            print(-1)
    else :
        print('err_case')