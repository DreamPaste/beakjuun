import sys

for line in sys.stdin:
    n = int(line.strip())
    seen = set()
    k = 0
    while True:
        k += 1
        num_str = str(n * k)
        for c in num_str:
            seen.add(c)
        if len(seen) == 10:
            print(k)
            break