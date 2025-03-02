import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
n = len(arr)
result = [-1] * n     
stack = []              

for i, num in enumerate(arr):
    # 스택이 비어있지 않고, 현재 num이 스택의 top 인덱스에 해당하는 값보다 크면
    while stack and arr[stack[-1]] < num:
        idx = stack.pop()
        result[idx] = num
    stack.append(i)  # 현재 인덱스를 스택에 추가


print(" ".join(map(str, result)))