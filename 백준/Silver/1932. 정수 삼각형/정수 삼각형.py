n = int(input())
data= []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            data[i][j] += data[i-1][j]
        elif i==j:
             data[i][j] += data[i-1][j-1]
        else:
            data[i][j] += max(data[i-1][j-1],data[i-1][j])
       
print(max(data[n-1]))