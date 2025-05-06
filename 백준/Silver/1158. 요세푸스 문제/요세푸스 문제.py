import collections
n,k = map(int, input().split())
que = collections.deque()
res=[]
idx = 1
for i in range(1, n+1):
    que.append(i)
while que :
    t = que.popleft()
    if idx == k :
        res.append(str(t))
        idx =1
    else :
      que.append(t)
      idx +=1
print("<"+ ", ".join(res) +">")