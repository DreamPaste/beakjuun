from collections import deque

n = int(input())
sequence = [int(input()) for _ in range(n)]
stack =deque()
top =1
operator =[]
for num in sequence :
    
    #stack의 top이 원하는 숫자가 될 때까지 push
    while top <= num :
        stack.append(top)
        operator.append("+")
        top+=1

    if stack[-1] == num :
        stack.pop()
        operator.append("-")
    
    else :
        operator = ["NO"]
        break

print("\n".join(operator))