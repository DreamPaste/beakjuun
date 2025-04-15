def backtrack(start, sequence):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    for i in range(start, n):
        backtrack(i, sequence + [numbers[i]])

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))
backtrack(0, [])
