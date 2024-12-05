from collections import deque
import sys
Queue = deque()
input = sys.stdin.readline

for i in range(int(input())) :
    line = list(input().split())
    command = line[0]

    if command == "push" :
        Queue.append(int(line[1]))
    
    if command == "pop" :
        if len(Queue) != 0 :
            print(Queue.popleft())
        else :
            print(-1)
    if command == "size" :
        print(len(Queue))

    if command == "empty" :
        if len(Queue) == 0 :
            print(1)
        else :
            print (0)
    
    if command == "front" :
        if len(Queue) != 0 :
            print(Queue[0])
        else :
            print(-1)

    if command == "back" :
        if len(Queue) != 0 :
            print(Queue[-1])
        else :
            print(-1)


