import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):
    # 앞뒤 공백 및 개행 제거 후 split()
    command = input().strip().split()
    op = command[0]
    
    if op == "all":
        S = set(range(1, 21))
    elif op == "empty":
        S = set()
    else:
        x = int(command[1])
        if op == "add":
            S.add(x)
        elif op == "remove":
            # S.remove(x)는 x가 없으면 에러 발생하므로, S.discard(x) 사용
            S.discard(x)
        elif op == "check":
            sys.stdout.write("1\n" if x in S else "0\n")
        elif op == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
