import sys
from collections import deque

sudoku=[]
blank=deque()
for i in range(9) :
    line = list(map(int,sys.stdin.readline().split()))
    sudoku.append(line)
    for j in range(9):
        if line[j] == 0:
            blank.append((i,j))

#print(blank)
def check(i, j, n):
    for t in range(9):
        #row check
        if n == sudoku[i][t]:
             return False
        #column check
        if n == sudoku[t][j]:
             return False
        
    #box check
    bx = (i//3)*3
    by = (j//3)*3
    for x in range(3):
        for y in range(3):
             if sudoku[x+bx][y+by] == n:
                  return False
             
    #해당 칸에 이 숫자가 들어갈수 있다면
    #print(f'{n}can in[{i},{j}]')         
    return True
             
def backTracking():

    if len(blank) == 0 :
         for line in sudoku:
              print(' '.join(map(str,line)))
         sys.exit(0)
    (i,j) =blank[0]
    for n in range(1,10):
        
        if check(i,j,n):
                
                sudoku[i][j] = n
                blank.popleft()
                backTracking()
                sudoku[i][j] = 0
                blank.appendleft((i,j))



backTracking()

    
