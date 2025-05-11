import sys
input = sys.stdin.readline

q = int(input())
res = []

for _ in range(q):
    a = int(input())
    if (a & -a) == a:
        res.append("1")
    else:
        res.append("0")

sys.stdout.write("\n".join(res) + "\n")