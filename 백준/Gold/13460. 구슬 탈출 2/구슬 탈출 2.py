#세로 N,가로 M, 가장 바깥은 막혀있음.
#판에 구멍이 하나 있고, 빨간 구슬만을 빼내는 게임
#중력을 이용해서 4방향으로 기울이기 가능
#각각의 동작에서 공은 동시에 움직임
#더 이상 구슬이 움직이지 않을 때까지 기울임
#최소 몇 번 만에 빨간 구슬을 빼낼 수 있는지 구하기

#첫 번째 줄에 N,M이 주어짐
#다음 N개의 줄에 M길이의 문자열이 주어짐
# '.': 빈칸
# '#': 벽
# 'O': 구멍
# 'R': 빨간 구슬
# 'B': 파란 구슬


from collections import deque

N, M = map(int,input().split(' '))
board = []

for i in range(N):
    board.append(list(input().strip()))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class State:
    def __init__(self, red, blue, depth):
        self.red = red
        self.blue = blue
        self.depth = depth

# red, blue, hole의 위치를 보드에서 찾아 반환함
def find():
    for i in range(N):
        for j in range(M):

            if board[i][j] == 'R':
                red = Ball(i,j)
                #구슬이 있단 위치를 빈 칸으로..
                board[i][j] = '.'
            elif board[i][j] == 'B':
                blue = Ball(i,j)
                board[i][j] = '.'
            elif board[i][j] =='O':
                hole = Ball(i,j)
    return red, blue, hole

# 보드를 기울임(공이 해당 방향의 끝가지 움직임) 공이 움직인 거리 반환.
def move(ball, dx, dy, hole):
    step= 0

    while(board[ball.x + dx][ball.y + dy] != '#') :
        
        ball.x += dx
        ball.y += dy
        step+=1

        # 구멍에 들어가면 멈춤
        if(ball.x, ball.y) == (hole.x, hole.y):
            break
    
    return step


def bfs(init_red, init_blue, hole):
    visited =set()
    directions = [(0,-1), (0,1), (1,0), (-1,0)]
    que = deque()

    que.append(State(init_red, init_blue, 0))
    
    visited.add(
        (init_red.x,init_red.y, init_blue.x, init_blue.y))
    
    while que:
        #공들의 상태를 꺼냄
        state = que.popleft()

        if state.depth >= 10:
            return -1

        # 4방향으로 보드를 기울임
        for dx, dy in directions: 
            #새로운 객체 생성
            red = Ball(state.red.x, state.red.y)
            blue = Ball(state.blue.x, state.blue.y)
            
            red_step = move(red, dx, dy, hole)
            blue_step = move(blue, dx, dy, hole)

            # 파란 구슬이 구멍에 빠질경우
            if (blue.x, blue.y) == (hole.x, hole.y):
                continue

            # 빨간 구슬이 구멍에 빠질경우
            if(red.x, red.y) == (hole.x, hole.y):
                return state.depth + 1
            
            # 구슬이 같은 위치에 있는 경우

            if(red.x, red.y) == (blue.x, blue.y):
                #빨간 구슬이 멀리서 온 경우

                if(red_step> blue_step):
                    red.x -= dx
                    red.y -= dy
                else: 
                    blue.x -= dx
                    blue.y -= dy
            
            #방문 처리 및 큐에 추가
            now_pos = (red.x ,red.y, blue.x, blue.y)
            if now_pos not in visited:
                #방문처리
                visited.add(now_pos)
                #큐에 추가
                que.append(State(red, blue, state.depth+1))

    #모든 방문 처리를 했음에도 -1 이 출력 안되는 경우(Case7)
    return -1





red, blue, hole = find()
print(bfs(red, blue, hole))