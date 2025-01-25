import sys

input = sys.stdin.readline

data = input().strip()
#cursor: 0 a1 b2 c3 d4
M = int(input())
cursor = len(data)

left_stack = list(data)
right_stack = []

for _ in range(M):
    command = input().strip().split()
    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])
    else:
        print("unexpected input error")

result = ''.join(left_stack + right_stack[::-1])
print(result)