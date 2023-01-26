#변수 설정
from collections import deque
import sys
input = sys.stdin.readline
dx,dy = [-1,1,0,0],[0,0,-1,1]
ans=1

#입력
r,c = map(int,input().split())
data = [list(input()) for _ in range(r)]


#간선 비용이 없으므로  bfs를 이용한 탐색
def bfs() :
    global ans 
    queue = set([(0,0,data[0][0])]) 
    #시간을 줄이기 위해 set이용, 처음 시작 좌표와 해당 데이터 입력

    while queue:
        x,y,visit = queue.pop()
        ans = max(ans,len(visit))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx <r and 0<=ny <c:
                if data[nx][ny] not in visit: #중복되지 않을때
                    queue.add((nx,ny,visit+data[nx][ny]))

bfs()
print(ans)
