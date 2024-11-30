

line = input()
num =0
minuend =0 # 감수(뺄 숫자)
SUBMOD = False

for char in line :


    
    # - 가 한번이라도 나오면 그떄부터 나오는 수는 다 뺀다.
    if char == '-' : 
        
        if not SUBMOD :
            minuend += num
            num = 0
        else :
            minuend -= num
            num = 0
        SUBMOD = True

    elif char =='+' :
        if not SUBMOD:
            minuend+= num
            num = 0
        
        else :
            minuend-= num
            num =0
            
    else:
        num = num*10 + int(char)

if SUBMOD :
    minuend -= num
else :
    minuend += num
    
print(minuend)

    
    

   

    
    