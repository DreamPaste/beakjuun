# # 아무 의견이 없다면 문제의 난이도는 0
# # 의견이 하나 이상 있다면, 난이도는 전체의 30% 절사평균
import sys 
input = sys.stdin.readline
def round2(num) :
    if num - int(num) >= 0.5 :
        return int(num) + 1
    return int(num)

n = int(input())
data =[]
if n == 0 : 
    print(0)
else :
    
    for i in range(n) :
        data.append(int(input()))

    data.sort()
    div_num = round2(n * 0.15)
    sum_number = sum(data[div_num : n - div_num])
    cnt = n - 2*div_num

    print(round2(sum_number/cnt))
    




