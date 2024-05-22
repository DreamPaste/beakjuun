import sys
from collections import deque

# 1,...,i-2, i-1, i, i+1, i+2,....N,1(원형)
N = int(input())
cmds  = list(map(int,sys.stdin.readline().strip().split()))

nums = deque(i for i in range(1, N+1))
res=[]
#deq.rotate() 사용

while nums:
    i = nums.popleft()
    
    res.append(i)
    cmd = cmds[i-1]
    #print('cmd:',cmd)
    forRotateCmd= 1-cmd if (cmd>0) else -(cmd)
    #print('forR:',forRotateCmd)
    #print('before',nums)
    nums.rotate(forRotateCmd)
    #print('after',nums)
print(' '.join(map(str,res)))