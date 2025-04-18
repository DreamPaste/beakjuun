a, b = map(int, input().split())
arr = list(map(int, input().split()))
area = a * b
for i in range(5):
    arr[i] -= area
print(' '.join(map(str, arr))) 
