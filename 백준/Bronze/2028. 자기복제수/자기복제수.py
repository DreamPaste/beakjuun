for i in range(int(input())):
    num = int(input())
    sqar = str(num**2)
    if str(num) == sqar[-len(str(num)):] :
        print('YES')
    else :
        print('NO')