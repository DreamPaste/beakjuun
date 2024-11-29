
N = int(input())
data = list(map(int, input().split()))
prefix =[0] * (N+1)
data.sort()
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + data[i-1]

print(sum(prefix))