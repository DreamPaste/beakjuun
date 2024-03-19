#백준 2164

#1번이 큐의 제일 위에, N번이 제일 밑에 있음
#위에 있는 카드를 버리고, 그 다음 카드를 아래로 옮김
#마지막 남은 카드 하나 출력
from collections import deque

queue = deque()

N = int(input())

for i in range(1,N+1):
    queue.append(i)

while(True):
    if(len(queue) == 1):
        print(queue.popleft())
        break
    else:
        queue.popleft()
    queue.append(queue.popleft())
   