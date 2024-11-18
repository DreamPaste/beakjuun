

N, K = map(int, input().split()) # max N = 100000, K = N-1
data = list(map(int, input().split()))
temp = [0 for i in range(N)]
temp[0] = data[0]
for i in range(1,N):
    temp[i] = temp[i-1] + data[i]


res =temp[K-1]
#temp[2] - temp[0]
#data[0] + data[1] + data[2] - data[0]
#data[0+1] - 0
#temp[1] - 0

for i in range(K,N):
    if res < temp[i]-temp[i-K] : 
        res = temp[i] - temp[i-K]

print(res)
    

