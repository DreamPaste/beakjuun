data = []

for i in range(3):
    line = input()

    if line =='FizzBuzz':
        #해당 수는 3과 5로 나누어 떨어집니다.
        continue
       
    elif line == 'Fizz' : 
        #해당 수는 3의 배수입니다.
        continue
        
    elif line == 'Buzz' :
        #해당 수는 5로 나누어 떨어집니다.
        continue
    else :
        num = int(line) + 3 - i
        if num % 15 == 0 :
            print('FizzBuzz')
        elif num % 3 == 0 :
            print('Fizz')
        elif num % 5 == 0 : 
            print('Buzz')
        else :
            print(num)

        break