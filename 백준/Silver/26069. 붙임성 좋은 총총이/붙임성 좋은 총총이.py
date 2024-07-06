
import sys
dance =set()
dance.add("ChongChong")
n = int(sys.stdin.readline())
for i in range(n):
    meet = (sys.stdin.readline().strip().split(' '))
    if meet[0] in dance : 
        dance.add(meet[1])
    elif meet[1] in dance :
        dance.add(meet[0])

print(len(dance))