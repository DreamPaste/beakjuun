import sys
input = sys.stdin.read

N, M, *nums = map(int, input().split())
nums.sort()

def dfs(seq):
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return
    for i in range(N):
        dfs(seq + [nums[i]])

dfs([])