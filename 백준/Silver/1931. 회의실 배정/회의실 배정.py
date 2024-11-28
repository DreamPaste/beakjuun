
n = int(input())
data =[list(map(int, input().split())) for _ in range(n)]
cnt =0
END =0
data.sort(key=lambda x: (x[1], x[0]))

for startTime, endTime in data:
    if startTime >= END:
        cnt+=1
        END = endTime
print(cnt)