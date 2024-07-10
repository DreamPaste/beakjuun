

n = int(input())
res = [[' '] * n for _ in range(n)]
def starRender(n,star,x,y):
    #print(f'starRender(n={n},star={star},x={x},y={y})')

    if(n<3):
        if(star == 1):
            res[x][y] ='*'
            #print('x,y : ',x,y,'*')
        else:
            res[x][y]= ' '
            #print('x,y : ',x,y,'_')
        return
    
    else:
        new_n = n//3

        for row in range(3):
            for col in range(3):

                if row == col == 1 :
                    #공백 출력
                    starRender(new_n,0, x+ new_n*row, y+ new_n*col)         

                else:
                    starRender(new_n,star, x+ new_n*row, y+ new_n*col)

       
    
starRender(n,1,0,0)

# 결과 출력
for row in res:
    print(''.join(row))