import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
target = int(input().strip())

arr.sort()

left, right = 0, n - 1
count = 0

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        count += 1
        left += 1
        right -= 1
    elif s < target:
        left += 1
    else:
        right -= 1

print(count)
