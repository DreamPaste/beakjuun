import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())

    clothes = {}
    
    for _ in range(n):
        item, category = input().strip().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
    
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    
    
    print(result - 1)