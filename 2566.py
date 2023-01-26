#최댓값
data =[]
for i in range(9) :
    data.append(list(map(int,input().split())))

max =0
mi=0
mj=0
for i in range(9):
    for j in range(9):
        if data[i][j] > max :
            max = data[i][j]
            mi = i
            mj = j

print(max)
print(mi+1,mj+1) #모든 입력값이 0일 경우 , 1,1을 출력