from math import ceil
R, C, N = map(int, input().split())  
row = ceil(R / N)
col = ceil(C / N)
print(row * col)