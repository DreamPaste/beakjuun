n = int(input())

# 첫 줄
print('@' * (n + 2))

# 중간 줄 (2 ~ N+1)
for _ in range(n):
    print('@' + ' ' * n + '@')

# 마지막 줄
print('@' * (n + 2))
