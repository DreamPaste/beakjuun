
from sys import stdin as s
from math import factorial as fac
for case in range(int(s.readline())):
    N, M = map(int, s.readline().strip().split())

    print(fac(M)//fac(M-N)//fac(N))