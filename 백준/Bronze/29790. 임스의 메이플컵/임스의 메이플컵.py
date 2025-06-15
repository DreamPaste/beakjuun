n, u, l = map(int, input().split())

boj = False
if n >= 1000:
    boj = True

if boj:
    if u >= 8000 or l >= 260:
        print('Very Good')
    else:
        print('Good')
else:
    print('Bad')
