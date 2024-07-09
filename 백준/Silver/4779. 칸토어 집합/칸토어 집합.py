
def cantor_set(n):
    
    if(n<3):
        return print('-',end='')
    
    else:
       for i in range(3):
            if i == 1 :
               for j in range(n//3):
                print(' ',end='')
            else :
               cantor_set(n//3)
            
            
           

while True:
    try:

        n = int(input())
        cantor_set(3**n)
        print()
    except:
      break