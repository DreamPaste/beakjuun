from itertools import combinations
from bisect import bisect_right

def get_subset_sums(arr):
    subset_sums = []
    n = len(arr)
    for i in range(n + 1):
        for comb in combinations(arr, i):
            subset_sums.append(sum(comb))
    return subset_sums


N, C = map(int, input().split())
weights = list(map(int, input().split()))

mid = N // 2
left = weights[:mid]
right = weights[mid:]

left_sums = get_subset_sums(left)
right_sums = get_subset_sums(right)
left_sums.sort()

count = 0
for r in right_sums:
    remain = C - r
    count += bisect_right(left_sums, remain)

print(count)
