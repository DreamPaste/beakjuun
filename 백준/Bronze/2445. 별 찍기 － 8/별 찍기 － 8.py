N = int(input())
for i in range(1, N + 1):
        stars = '*' * i
        spaces = ' ' * (2 * (N - i))
        print(stars + spaces + stars)
    
   
for i in range(1, N):
        stars = '*' * (N - i)
        spaces = ' ' * (2 * i)
        print(stars + spaces + stars)