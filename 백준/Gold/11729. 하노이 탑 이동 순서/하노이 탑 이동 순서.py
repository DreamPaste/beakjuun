

n = int(input())
res=[]

def hanoi(n,start,end,temp):
    global res
    if n == 1:
        res.append(f"{start} {end}")
        return
    else:
        hanoi(n-1, start, temp, end) # start pole에서 temp pole로 이동
        res.append(f"{start} {end}")
        hanoi(n-1, temp, end, start) # temp pole에서 end pole로 이동

hanoi(n,1,3,2)
print(len(res))
for line in res :
    print(line)