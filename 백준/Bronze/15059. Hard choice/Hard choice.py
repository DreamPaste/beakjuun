available = map(int, input().split())
request = map(int, input().split())
total = 0
for a, r in zip(available, request):
    if a < r:
        total += (r - a)

        
print(total)