

n_len = int(input())

n_list = list(map(int,input().split()))

operator = list(map(int,input().split()))


res= set()

def calculate (input_A, input_B, op) :

    if op == 0 :
        return input_A + input_B
    
    if op == 1 :
        
        return input_A - input_B
    
    if op == 2 :
        
        return input_A * input_B
    
    if op == 3 and input_A<0 and input_B >0:
        return -(abs(input_A) // input_B)
    
    else :
        return input_A // input_B


    
def backtracking(idx, num):

    if n_len-1 == idx:
        res.add(num)
        
        
    
    for i in range(4):
        
        if  operator[i] >0:
            operator[i] -= 1
            next_num = n_list[idx+1]

            new_num = calculate(num, next_num, i)
            
            backtracking(idx+1, new_num)
            #이전 상태로 복귀
            operator[i] += 1
            
   


backtracking(0, n_list[0])

print(max(res))
print(min(res))