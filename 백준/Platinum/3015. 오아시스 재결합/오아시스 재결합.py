import sys

input = sys.stdin.readline
n = int(input().strip())  # 사람의 수
result = 0
stack = []  # 스택: 각 요소는 (키, count) 튜플
    
for _ in range(n):
    h = int(input().strip())
    count = 1  # 같은 키가 연속된 경우를 세기 위한 변수
    
    # 스택에서 현재 사람보다 작은 사람들을 모두 제거
    while stack and stack[-1][0] < h:
        result += stack[-1][1]
        stack.pop()
    
    # 스택의 맨 위에 같은 키를 가진 사람이 있으면
    if stack and stack[-1][0] == h:
        same_count = stack[-1][1]
        result += same_count
        stack.pop()
        count = same_count + 1  # 같은 키의 개수를 1 증가
        # 스택에 남아 있다면, 그 사람과도 볼 수 있으므로 1 추가
        if stack:
            result += 1
    # 스택에 남아있는 사람이 현재 사람보다 큰 경우
    elif stack:
        result += 1
    
    # 현재 사람을 스택에 추가
    stack.append((h, count))
print(result)