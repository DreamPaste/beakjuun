t = int(input())
for _ in range(t):
    n = int(input())
    binary = bin(n)[2:]
    for i in range(len(binary)):
        if binary[-(i + 1)] == '1':
            print(i, end=' ')
    print()