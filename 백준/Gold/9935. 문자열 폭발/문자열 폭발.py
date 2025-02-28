import sys

def input(): return sys.stdin.readline()

def arrToString(arr) : return ''.join(arr)
string = input().strip()
explosion = input().strip()

stack = []

for char in string:
    stack.append(char)

    if len(stack) >= len(explosion) and arrToString(stack[-len(explosion):]) == explosion:
        del stack[-len(explosion):]

result = arrToString(stack)

print(result if result else "FRULA")