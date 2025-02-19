N, M = map(int, input().split())
data ={}
for i in range(N):
    site, password = input().split()
    data[site] = password

for i in range(M):
    print(data[input()])