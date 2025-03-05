import sys

input = sys.stdin.readline

N = int(input())  # 1 <= N <= 100,000

histogram = []
for _ in range(N):
    histogram.append(int(input().strip()))

stack = []  # 인덱스를 저장하는 스택
ans = 0

for i in range(N):
    # 현재 막대가 스택 top의 막대보다 작을 때까지 pop하며 넓이 계산
    while stack and histogram[stack[-1]] > histogram[i]:
        top = stack.pop()
        height = histogram[top]
        if stack:
            width = i - stack[-1] - 1
        else:
            width = i
        ans = max(ans, height * width)
    stack.append(i)

# for 루프 종료 후 스택에 남은 인덱스들 처리
while stack:
    top = stack.pop()
    height = histogram[top]
    if stack:
        width = N - stack[-1] - 1
    else:
        width = N
    ans = max(ans, height * width)

print(ans)
